#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-12-27
@author: ymy
Copyright ymyjohnny@gmail.com
'''


#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2015-12-25
@author: Shell.Xu
@copyright: 2015, Shell.Xu <shell909090@gmail.com>
@license: cc
'''
import re
import sys
import gzip
import datetime
import pandas

headers = ['ipaddr', 'date', 'method', 'path', 'version', 'headline',
           'status', 'time', 'reference', 'agent']
re_log = re.compile('(?P<ipaddr>\S*) - (?P<user>\S*) \[(?P<date>.*) \+0800\]\s+"((?P<method>\S*) (?P<path>\S*) (?P<version>\S*)|(?P<headline>.*))" (?P<status>\d*) (?P<size>\d*) (?P<time>[0-9\.]*) "(?P<reference>.*)" "(?P<agent>.*)"')
dt_fmt = '%d/%b/%Y:%H:%M:%S'

def parser(line):
    line = line.strip()
    m = re_log.match(line)
    assert m, Exception(line)
    d = m.groupdict()
    d['date'] = datetime.datetime.strptime(d['date'], dt_fmt)
    return d

def log_source(filepath):
    with gzip.open(filepath) as fi:
        for line in fi:
            yield parser(line)

def main():
    #dataFrame  序列集合，把之前字典的集合拆分成序列集合
    dt = pandas.DataFrame(log_source(sys.argv[1]))
    #dt.info()
    #dt.ipaddr.value_counts() 统计ipaddr的count
    #d = dt[dt.ipaddr != '192.168.1.311']
    #去除192.168开头的
    dt = dt[~dt.ipaddr.str.startswith('192.168')]
    #去除监控包的数据
    dt = dt[~dt.agent.str.contains('JianKongBao')]
    #去除status 等于304的
    dt = dt[dt.status != '304']
    print dt.info()
    
    #2种方法获取每小时访问量
    vc = dt.date.map(lambda x: x.hour).value_counts(sort=False)
    vc.plot().get_figure().savefig('web-nginx-1.jpg')
    #2种方法获取每小时访问量
    dt['date_dt'] = dt.date.map(lambda x: x.hour)
    dt.groupby(['date_dt']).count()['status'].plot().get_figure().savefig('web-nginx-2.jpg')

if __name__ == '__main__': main()