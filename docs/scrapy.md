# scrapy 教程
## 核心组件信息统计

```
ons.telnet] DEBUG: Telnet console listening on 127.0.0.1:6024
engine.slot.inprogress

time()-engine.start_time                        : 8.62972998619
engine.has_capacity()                           : False
len(engine.downloader.active)                   : 16 请求正被下载器下载
engine.scraper.is_idle()                        : False
engine.spider.name                              : followall
engine.spider_is_idle(engine.spider)            : False
engine.slot.closing                             : False
len(engine.slot.inprogress)                     : 16 
len(engine.slot.scheduler.dqs or [])            : 0
len(engine.slot.scheduler.mqs)                  : 92  有92请求（mqs）在队列中等待处理
len(engine.scraper.slot.queue)                  : 0	
len(engine.scraper.slot.active)                 : 0 正有0个响应在scraper中处理
engine.scraper.slot.active_size                 : 0
engine.scraper.slot.itemproc_size               : 0 pipeline中正有0个item在被处理
engine.scraper.slot.needs_backout()             : False


阻塞显示 1
time()-engine.start_time                        : 636.3400275707245
engine.has_capacity()                           : False
len(engine.downloader.active)                   : 1
engine.scraper.is_idle()                        : False
engine.spider.name                              : spu_jd
engine.spider_is_idle(engine.spider)            : False
engine.slot.closing                             : False
len(engine.slot.inprogress)                     : 1
len(engine.slot.scheduler.dqs or [])            : 0
len(engine.slot.scheduler.mqs)                  : 0
len(engine.scraper.slot.queue)                  : 0
len(engine.scraper.slot.active)                 : 0
engine.scraper.slot.active_size                 : 0
engine.scraper.slot.itemproc_size               : 0
engine.scraper.slot.needs_backout()             : False
```
