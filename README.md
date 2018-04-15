# bug-monitor
Seebug、structs、cve漏洞实时监控推送系统


[![GitHub issues](https://img.shields.io/github/issues/FortuneC00kie/bug-monitor.svg)](https://github.com/FortuneC00kie/bug-monitor/issues)
[![GitHub forks](https://img.shields.io/github/forks/FortuneC00kie/bug-monitor.svg)](https://github.com/FortuneC00kie/bug-monitor/network)
[![GitHub stars](https://img.shields.io/github/stars/FortuneC00kie/bug-monitor.svg)](https://github.com/FortuneC00kie/bug-monitor/stargazers)
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) 
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/FortuneC00kie/bug-monitor/master/LICENSE)


## 特性

通过爬虫实时爬取seebug、structs等的页面，若发现有新的漏洞出现，存入mongodb并可通过微信公众号进行推送（此项功能需要在config.ini中配置app_key和secuity）程序默认保存一个月之内的漏洞，超过一个月的漏洞会被自动清理

程序使用的微信推送功能和cve信息爬取的配置信息都要在config.yaml中配置（ps：cve信息爬取使用的api是https://www.saucs.com 因此需要去该网站注册账号并查看自己的api信息进行配置）

本项目还使用了chrome headless进行反爬虫绕过，因此需要安装chromedriver依赖，详情可参考[链接](https://www.cnblogs.com/technologylife/p/5829944.html)

## todo
1.实现对cnnvd等监控

2.结合github泄漏监控做到微信公众号推送

3.针对不同用户需求，实现微信公众号差异化推送