#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

from bs4 import BeautifulSoup
import requests
import re
import sys
from lib.mongodb import *
from lib.log import *


def struts_latest():
    try:
        struts = requests.get("https://cwiki.apache.org/confluence/display/WW/Security+Bulletins", timeout=5)
    except Exception as e:
        exception(e)
    soup = BeautifulSoup(struts.text, "html.parser")
    s2 = soup.find_all(href=re.compile("S2-"))
    return s2.pop()


def struts_info(url, struts_id):
    try:
        s2_page = requests.get(url)
    except Exception as e:
        exception(e)
    soup = BeautifulSoup(s2_page.text, "html.parser")
    content = soup.tbody
    name = struts_id
    rate = content.findAll('p')[5].string
    affected = content.findAll('p')[9].get_text()
    cveid = content.findAll(text=re.compile("CVE-"))
    if cveid:
        cveid = content.findAll(text=re.compile("CVE-"))[0].string
    else:
        cveid = None
    info = soup.find(id=struts_id+"-Problem").find_next().get_text()
    i = {'name': name, 'rate': rate, 'affected': affected, 'cveid': cveid, 'info': info}
    return i


def struts_info_save(url, struts_id):
    i = struts_info(url, struts_id)
    if not bug_info_search(i['name']):
        bug_info_save(i['name'], i['rate'], i['affected'], i['info'], i['cveid'], url, None)


def struts_init():
    s2_last = struts_latest()
    struts_id = s2_last.string
    s2_url = "https://cwiki.apache.org" + s2_last['href']
    if not bug_info_search(struts_id):
        struts_info_save(s2_url, struts_id)
    info("struts bug info init success!")
