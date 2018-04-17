#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)

from selenium import webdriver
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/65.0.3325.181 Safari/537.36'}

def cookie_init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    client = webdriver.Chrome(chrome_options=chrome_options)
    client.get("https://www.seebug.org/vuldb/vulnerabilities")
    client.get("https://www.seebug.org/vuldb/vulnerabilities")
    cookie = {}
    for item in client.get_cookies():
        cookie[item["name"]] = item["value"]
    client.quit()
    s = requests.session()
    s.headers.update(headers)
    requests.utils.add_dict_to_cookiejar(s.cookies, cookie)
    return s


