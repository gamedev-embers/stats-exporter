# 简介
丐版实时数据分析服务，小/穷团队的救星。  
本项目用于实时统计游戏运营数据指标，导出到 prometheus 或者 csv 文件. 业务端只需提供指定格式的日志流即可.

# 繁介
游戏项目上线后需要频繁查看运营数据指标，为团队接下来的功能迭代提供决策依据。
理想情况下，团队可以花钱租一套提供丰富业务指标的数据分析服务，但更多时候会因为暂不需要重度使用(简单说就是穷)而选择廉价方案——客户端的三方数据服务。
但仅靠这个是不够的，你还需要服务端的数据分析做为对照和补充。这其中包含离线分析和实时分析任务，前者可以用对象存储服务+OLAP系统来实现(比如 S3+PrestoSQL)，
后者你经过一番调研，没发现什么好用方案，净是一堆 spark steaming, flink 吓死人的大数据重器。咋办？于是你上 github 找替代方案，冥冥之中看到了这里。
接着花 5 分钟适配日志流后就用上了。

后续…… 你可能会有两种体验
1. “哎哟，不错哟”，于是帮助作者开发。
2. “什么破玩儿“，于是帮助作者改善。

总之你决定帮助作者。

# Status
dev


# 特性
* ~~超低资源占用率（计数器使用 hyperloglogs）~~
* ~~支持常用运营指标，(D/M/W)AU, (D/M/W)NU, ARPU, ARPPU 等等~~
* ~~支持导出到 prometheus~~
* **目前啥都没实现**


# TODO
- [ ] 设计一套标准的审计日志，要简单易用，5分钟内看懂。
- [ ] 活跃相关指标
- [ ] 付费相关指标
- [ ] metrics exporter 
- [ ] 提供 http api 供查询

# 容量预览（理论上）
* 100w 个 24 字节 id 大约是 24MB 。


# FAQ
