#coding:utf-8
import requests
from seebug_cookie_init import cookie_init
from lxml import etree
import time, sys
import sys
import time

sys.path.append("..")
from lib.mongodb import *

reload(sys)
sys.setdefaultencoding('utf-8')


url = 'https://www.seebug.org/vuldb/vulnerabilities'
aburl  = 'https://www.seebug.org'

headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}

def seebug_crawer():
    cookie = cookie_init()
    s = requests.session()
    requests.utils.add_dict_to_cookiejar(s.cookies, cookie)
    content = s.get(url).content
    ahref = get_bug_link(content)
    get_bug_content(ahref, s)

def get_bug_content(ahref, s):
    for a in ahref:
        r2 = s.get(url=aburl+a, verify=False)
        time.sleep(5)
        if r2.status_code==403:
            print '403 error'
            time.sleep(20)
            r2=s.get(url=aburl+a,verify=False)
        print 'content code---------------'
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
    tree=etree.HTML(content)
    ahref=tree.xpath("//table[@class='table sebug-table table-vul-list']//tr//td[@class='vul-title-wrapper']/a[@class='vul-title']/@href")
    return ahref