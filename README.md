# bug-monitor
Seebug、structs、cve漏洞实时监控推送系统

## 特性

通过爬虫实时爬取seebug、structs等的页面，若发现有新的漏洞出现，存入mongodb并可通过微信公众号进行推送（此项功能需要在config.yml中配置app_key和secuity）程序默认保存一个月之内的漏洞，超过一个月的漏洞会被自动清理

## todo-list
1.实现对cnnvd等监控

2.结合github泄漏监控做到微信公众号推送

3.针对不同用户需求，实现微信公众号差异化推送
