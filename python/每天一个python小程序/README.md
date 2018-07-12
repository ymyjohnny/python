# python每天一个小程序

2015-11-22 grep 用第一个文件中的行逐行过滤第二个文件的内容，并打印出第一个文件中没有匹配到的行

2015-11-23 取出java进程的进程号

2015-11-24 过滤关键字，replace替换filter_word.txt中的关键字为星号

2015-11-25 从config20151124.json中读取json格式的配置，加入当前时间datetime，并写入到mongodb的ymytest库的test1表中

2015-11-26 获取线上所有服务器的基础信息，存入mongodb

2015-11-27 从mongodb读取服务器基础信息，打印出hostname

2015-11-28 发送mail.txt的文本内容到163邮箱，支持中文

2015-11-29 从wenku8.com爬小说，输出到txt

2015-12-08 查询mongo服务状态.py

2015-12-09 diff 文件

2015-12-10 diff 目录

2015-12-15 mysql和mongo值对比.py

2016-01-22 随机数.py

2016-05-17 checkmongofc.py 迁移mongo过程中新fc和老fc之间的量

2016-05-20 redisclusterinstantaneous.py 查看redis集群每个节点的实时请求量

2016-05-23 dspdumpview.py 查询mysql中某张view的数据

2016-06-01 redisclusterslavebehind.py 查询redis集群各节点的slave延迟时间

2016-06-01 redisclusterslavestatus.py 查询redis集群各节点的slave状态

2016-06-22 mongoaddindex.py 给mongo某个表添加索引

2016-06-22 mongo-index-check.py 检查mongo库的索引

2016-06-27 获取mongostatus.py 查看mongo某个表的status

2016-07-14 pingcheck.py 监测机房网络工具

2016-10-26 check出价没有赢价.py 列出检查有出价没有赢价的投放

2016-10-28 循环中断

2016-11-15 连接redis.py

2017-04-10 查询dsp里各个延迟类别是否超过阀值

2017-04-28 通过nodetool命令查看cassandra表的状态（读写count是累计值，通过写文件做2次取值的差值）

2017-05-03 通过nodetool命令查看cassandra表的状态

2017-05-05 winnotice的errorlog监控

2017-05-11 检查是否有visitlog，加入小米监控

2017-05-25 查看flume状态

2017-06-02 统计各家adx的visitlog和mobilelog，加入小米监控

2017-06-07 检查mongo内存，加入小米监控

2017-06-08 检查dsp昨天的投放状态，超量则会发邮件报警

2017-06-21 redis扫描各种key的行数，加入小米监控

2017-06-28  定期清理mongo_unionfc的库，根据订单id和活动id 保留3个月

2017-07-24  分析winnotice的超时过滤，写入mongo

2017-07-25  从mongo中读取超时的winnotice记录，发送邮件报警

2017-08-09  每天从日志里获取统一id、日志类型、更新时间、订单id 写入mongo

2017-08-10  根据条件从mongo中读取信息写入文件

2017-09-04  查询mysql中的dsp报表,写入csv文件

2017-09-28  比对winnotice的赢价时间和bidder出价时间写入数据库(需要unix和dt时间转换)

2017-11-15  比对文件1和文件2中重合的idfa个数

2017-12-01  检查10分钟前的各渠道的ecpm价格,提交到falcon

2017-12-06  统计昨天一天的各渠道平均cpm及投放量

2018-02-28 两个数的加减乘除函数

2018-02-28 模拟UA访问网站

2018-03-01 查询mongo函数

2018-03-02 tornado框架查询mongo

2018-05-24 每天上线的活动及订单
