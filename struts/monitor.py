#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
import sys
sys.path.append("..")

from struts.init import struts_latest, struts_info
from lib.wechat import *
from lib.mongodb import *

def struts_check():
    a = struts_latest()
    if not bug_info_search(a.string):
        url = "https://cwiki.apache.org" + a['href']
        i = struts_info(url, a.string)
        msg = u"0DAY: " + i['name'] + "\r\n" + u"影响范围: " + i['affected'] + "\r\n" + u"漏洞评级: " + i['rate'] + "\r\n"\
              + u"CVE编号: " + i['cveid'] + "\r\n" + u"摘要: " + i['info']  + "\r\n" + "Refer: " + url
        send_wechat(msg)
        bug_info_save(i['name'], i['rate'], i['affected'], i['info'], i['cveid'], url)