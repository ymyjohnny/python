#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-7-14
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import commands
import time
import requests
import json

def get_delay(ip):
    host=str(ip)
    host=host.lstrip()
    host=host.rstrip()

    host=host.expandtabs()
    host=host.replace(' ','.')
    host=host.replace('|','.')

    command="ping -c1 -W1 " + host + " | grep icmp_seq | awk '{print $7}' | cut -d '=' -f 2"
    result=commands.getoutput(command)

    try:
        return float(result)
    except:
        return 0

def payload(hostname,metric,ip):
    ts = int(time.time())
    value=get_delay(ip)
    data={"endpoint": hostname,"metric": metric,"timestamp": ts,"step": 60,"value": value,"counterType": "GAUGE","tags": "",}
    return data

def post_data(config):
    data=[]
    for conf in config:
        load=payload(conf["hostname"],conf["metric"],conf["ip"])
        data.append(load)

    return data

if __name__ == '__main__':

    config=[
        {"hostname":"rs29.adsame.com","metric":"ip:60s-101.227.14.115","ip":"101.227.14.115"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-111.206.13.247","ip":"111.206.13.247"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-123.125.118.44","ip":"123.125.118.44"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-103.41.143.128","ip":"103.41.143.128"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-43.250.15.78","ip":"43.250.15.78"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-140.205.203.151","ip":"140.205.203.151"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-118.26.200.34","ip":"118.26.200.34"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-223.203.194.194","ip":"223.203.194.194"},
        {"hostname":"rs29.adsame.com","metric":"ip:60s-222.73.96.66","ip":"222.73.96.66"},
    ]

    data=post_data(config)

    r = requests.post("http://192.168.32.2:1988/v1/push", data=json.dumps(data))

    #print r.text
    print json.dumps(data)
