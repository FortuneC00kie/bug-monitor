# bug-monitor
Seebug、structs、cve漏洞实时监控推送系统

## 特性

通过爬虫实时爬取seebug、structs等的页面，若发现有新的漏洞出现，存入mongodb并可通过微信公众号进行推送（此项功能需要在config.yml中配置app_key和secuity）程序默认保存一个月之内的漏洞，超过一个月的漏洞会被自动清理

程序使用的微信推送功能和cve信息爬取的配置信息都要在config.yaml中配置（ps：cve信息爬取使用的api是https://www.saucs.com 因此需要去该网站注册账号并查看自己的api信息进行配置）

## todo-list
1.实现对cnnvd等监控

2.结合github泄漏监控做到微信公众号推送

3.针对不同用户需求，实现微信公众号差异化推送
