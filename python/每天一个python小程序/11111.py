#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-6-24
@author: ymy
Copyright ymyjohnny@gmail.com
'''


import sys
import pymongo
import time

readMongo = ["192.168.32.71", 27018]
writeMongo = ["192.168.32.71", 27018]

TABLE_NAME = "user_solution_impression"
FNV_64_INIT = 0xcbf29ce484222325L
FNV_64_PRIME = 0x100000001b3L
FNV_32_INIT = 0x811c9dc5
FNV_32_PRIME = 0x01000193
INT_MAX = 2147483647

class HashBuilder(object):
    def __init__(self, iTotal, iConstant):
        self.iTotal = iTotal
        self.iConstant = iConstant

    def append(self, obj):
        self.iTotal = self.iTotal * self.iConstant + stringHashCode(obj)
        self.iTotal &= 0xFFFFFFFF
        return self

    def toHashCode(self):
        return self.iTotal

def stringHashCode(value):
    h = 0;
    if (h == 0 and len(value) > 0):
        for x in value:
            h = 31 * h + ord(x)
            h &= 0xFFFFFFFF
    return h;

def blockID(id):
    builder = HashBuilder(23,13)
    builder.append(id)
    hc = builder.toHashCode()
    hc = (~hc & 0xFFFFFFFF) +1 if hc > INT_MAX else hc
    return hc

def hash32(k):
    rv = FNV_32_INIT
    l = len(k)
    for i in range(l):
        rv ^= ord(k[i])
        rv *= FNV_32_PRIME
        rv &= 0xFFFFFFFF
    return  (~rv & 0xFFFFFFFF) +1 if rv > INT_MAX else rv

def main(index):
    start = time.time()
    rc = pymongo.MongoClient(readMongo[0], readMongo[1])
    wc = pymongo.MongoClient(writeMongo[0], writeMongo[1])
    rdb = rc.get_database("unionfc%s" % index)
    wdb = rc.get_database("unionfc%s" % (500 + index))
    rcol = rdb.get_collection(TABLE_NAME)
    print "begin process %s total count %s" % (index, rcol.count())
    wcol = wdb.get_collection(TABLE_NAME)
    rcur = rcol.find(batch_size=200)
    count = 0
    wcount = 0
    writeDocs = []
    for doc in rcur:
        count += 1
        if count % 1000 == 0:
            print "process count %s, write count %s" % (count, wcount)
        uid = doc['uid']
        blockid = blockID(uid)
        if blockid % 500 == blockid % 1000:
            continue
        writeDocs.append(doc)
        if len(writeDocs) > 100:
            wcol.insert_many(writeDocs)
            wcount += len(writeDocs)
            writeDocs = []

    if len(writeDocs) > 0:
        wcol.insert_many(writeDocs)
        wcount += len(writeDocs)
        writeDocs = []
    end = time.time()
    print "finish %s write count %s used %s" % (index, wcount, end-start)


if __name__ == "__main__":
    main(0)