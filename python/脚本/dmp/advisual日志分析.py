#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-1-8
@author: ymy
Copyright ymyjohnny@gmail.com
'''
a

import sys,re
import pandas


headers = ['logtype', 'daytime', 'ip', 'location', 'cookie', 'session','pointid', 'typeid', 'clickcid', 'clicksid', 'cilckbid', 'clicktime', 'cilckrefer', 'blank', 'logpara', 'cgid', 'refer','layoutid','siteid','channelgroupid','channelid','campaignid','orderid','solutionid','bannergoupid','bannerid','ua']

s_re_log = re.compile('(?P<logtype>\S*),(?P<daytime>.*),(?P<ip>\S*),(?P<location>\S*),(?P<cookie>\S*),(?P<session>\S*),(?P<layoutid>\d*),(?P<siteid>\d*),(?P<channelgroupid>\d*),(?P<channelid>\d*),(?P<campaignid>\d*),(?P<orderid>\d*),(?P<solutionid>\d*),(?P<bannergroupid>\d*),(?P<bannerid>\d*),(?P<ua>.*),"(?P<refer>.*)"')

t_re_log = re.compile('(?P<logtype>\S*),(?P<daytime>.*),(?P<ip>\S*),(?P<location>\S*),(?P<cookie>\S*),(?P<session>\S*),(?P<pointid>\d*),(?P<typeid>\d*),(?P<clickcid>\d*),(?P<clicksid>\d*),(?P<cilckbid>\d*),(?P<clicktime>\d*),"(?P<clickrefer>.*)",(?P<blank>\d*),"(?P<logpara>.*)",(?P<cgid>\d*),"(?P<refer>.*)"')
#re_log = re.compile('(?P<logtype>\S*),(?P<daytime>.*),(?P<ip>\S*),(?P<location>\S*),(?P<cookie>\S*),(?P<session>\S*),(?P<pointid>\d*),(?P<typeid>\d*),(?P<clickcid>\d*),(?P<clicksid>\d*),(?P<cilckbid>\d*),(?P<clicktime>\d*),"(?P<clickrefer>.*)"|"(?P<cilckrefer>\B)",(?P<blank>\d*),"(?P<logpara>.*)",(?P<cgid>\d*),"(?P<refer>.*)"')



def s_parser(line):
    line = line.strip()
    m = s_re_log.match(line)
    assert m, Exception(line)
    d = m.groupdict()
    return d


def t_parser(line):
    line = line.strip()
    m = t_re_log.match(line)
    assert m, Exception(line)
    d = m.groupdict()
    return d

def t_log_source(filepath):
    with open(filepath) as fi:
        for line in fi:
            if  line.startswith('t'):
                yield t_parser(line)
                

def s_log_source(filepath):
    with open(filepath) as fi:
        for line in fi:
            if  line.startswith('s'):
                yield s_parser(line)




def main():
    sid = sys.argv[2]
    tdt = pandas.DataFrame(t_log_source(sys.argv[1]))
    sdt = pandas.DataFrame(s_log_source(sys.argv[1]))
    print  '=========='
    tdt = tdt[tdt.clicksid == sid ]
    sdt = sdt[sdt.solutionid == sid]
    print tdt.info()

if __name__ == '__main__':
    main()
