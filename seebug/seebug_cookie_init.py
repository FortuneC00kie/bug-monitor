#coding:utf-8
from selenium import webdriver

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
    return cookie


