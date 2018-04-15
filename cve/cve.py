#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

import requests
import configparser
import sys
import time

from lib.mongodb import *

url = "https://api.saucs.com/cve"

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")


def cve_crawer():
	req = requests.Session()
	req.auth = (config.get("cve_api", "username"), config.get("cve_api", "password"))
	cve_list = req.get(url, auth = (config.get("cve_api", "username"), config.get("cve_api", "password")))
	a = cve_list.json()
	for i in range(len(a)):
		cve_url = url + '/' + a[i]['name']
		cve_info_page = req.get(cve_url)
		cve_info = cve_info_page.json()
		refer = cve_info['references'][0]['link']
		cveid = cve_info['name']
		info = cve_info['summary']
		print(cveid)
		if not cve_info_search(cveid):
			addtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			cve_info_save(info, cveid, refer, addtime)






