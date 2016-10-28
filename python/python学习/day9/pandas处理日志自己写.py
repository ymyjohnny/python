#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-1-10
@author: ymy
Copyright ymyjohnny@gmail.com
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
    dt = pandas.DataFrame(log_source(sys.argv[1]))
    dt = dt[~dt.ipaddr.str.startswith('192.168')]
    print dt.info()


if __name__ == '__main__':
    main()