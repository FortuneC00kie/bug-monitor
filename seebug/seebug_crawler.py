#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

from seebug.seebug_cookie_init import cookie_init
from lxml import etree
import time, sys
from lib.mongodb import *
from lib.log import *

url = 'https://www.seebug.org/vuldb/vulnerabilities'
aburl  = 'https://www.seebug.org'

def seebug_crawler():
    s = cookie_init()
    try:
        request = s.get(url, verify=False, timeout=5)
    except Exception as e:
        exception(e)
    if request.status_code == 521:
        info("seebug cookie init failed")
        s = cookie_init()
    content = request.content
    ahref = get_bug_link(content)
    get_bug_content(ahref, s)
    info("seebug crawl success")

def get_bug_content(ahref, s):
    for a in ahref:
        r2 = s.get(url = aburl+a, verify=False, timeout=5)
        time.sleep(5)
        if r2.status_code == 403:
            time.sleep(20)
            r2 = s.get(url = aburl+a,verify=False, timeout=5)
        if r2.status_code == 521:
            s = cookie_init()
            r2 = s.get(url = aburl+a,verify=False, timeout=5)
        tree2 = etree.HTML(r2.content)

        name = tree2.xpath("//span[@class='pull-titile']/text()")[0].strip()
        # try:
        #     href = tree2.xpath("//div[@id='j-md-source']/a/text()")[0].strip()
        #     print href
        # except IndexError:
        #     href = None
        try:
            app = tree2.xpath(u"//div[@class='row']/div/dl/dt[text()='影响组件：']/following-sibling::dd/a/text()")[0].strip()
        except IndexError:
            app = None
        # expose = tree2.xpath(u"//div[@class='row']/div/dl/dt[text()='披露/发现时间：']/following-sibling::dd/text()")[
        #     0].strip()
        _, rate = \
            tree2.xpath(
                u"//div[@class='row']/div/dl/dt[text()='漏洞等级：']/following-sibling::dd/div/@class")[
                0].strip().split(" ")
        # category = tree2.xpath(u"//div[@class='row']/div/dl/dt[text()='漏洞类别：']/following-sibling::dd/a/text()")[
        #     0].strip()
        cve = tree2.xpath(u"//div[@class='row']/div/dl/dt[text()='CVE-ID：']/following-sibling::dd/a/text()")[0].strip()
        # try:
        #     detail = tree2.xpath(u"//div[@id='j-md-detail']/text()")[0].strip()  # 图片只可以抓url地址
        # except IndexError:
        #     detail = None
        try:
            refer = tree2.xpath(u"//div[@class='solution-txt']/div[@class='padding-md']")[0].xpath('string(.)').strip().replace("\n", "")
            refer = refer.replace(" ", "")
        except IndexError:
            refer = url
        if not bug_info_search(name):
            addtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            bug_info_save(name, rate, app, None, cve, refer, addtime)


def get_bug_link(content):
    tree = etree.HTML(content)
    ahref = tree.xpath("//table[@class='table sebug-table table-vul-list']//tr//td[@class='vul-title-wrapper']/a[@class='vul-title']/@href")
    return ahref