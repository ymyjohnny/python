#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-11-15
@author:ymy
Copyright ymyjohnny@gmail.com
'''

'''参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行
'''

import redis
from rediscluster import StrictRedisCluster
import sys

def  redis_node():
    node = redis.StrictRedis(host='127.0.0.1',port=6379)
    node.set("name_test","admin")
    print node.get("name_test")

redis_node()

def redis_cluster():
    redis_nodes =  [{'host':'221.228.230.146','port':6370},
                    {'host':'221.228.230.146','port':6371},
                    {'host':'221.228.230.146','port':6372},
                    {'host':'221.228.230.146','port':6373},
                    {'host':'221.228.230.146','port':6374},
                    {'host':'221.228.230.146','port':6375},
                    {'host':'221.228.230.146','port':6376}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    redisconn.set('ymyname','admin')
    redisconn.set('ymyage',18)
    print "name is: ", redisconn.get('ymyname')
    print "age  is: ", redisconn.get('ymyage')

redis_cluster()

