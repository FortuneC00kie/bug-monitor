#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

import requests
import yaml
import sys
import time

sys.path.append("..")
from lib.mongodb import *

with open('config.yaml', 'r') as f:
	a = f.read()
	conf = yaml.load(a)

url = "https://api.saucs.com/cve"

def cve_crawer():
	req = requests.Session()
	req.auth = (conf['cve_api']['username'], conf['cve_api']['password'])
	cve_list = req.get(url, auth = (conf['cve_api']['username'], conf['cve_api']['password']))
	a = cve_list.json()
	for i in xrange(len(a)):
		cve_url = url + '/' + a[i]['name']
		cve_info_page = req.get(cve_url)
		cve_info = cve_info_page.json()
		refer = cve_info['references'][0]['link']
		cveid = cve_info['name']
		info = cve_info['summary']
		if not cve_info_search(cveid):
			addtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			cve_info_save(info, cveid, refer, addtime)






