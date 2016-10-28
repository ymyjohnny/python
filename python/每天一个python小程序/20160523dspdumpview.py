#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-5-23
@author: ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import pymongo

def get_view(view):
    conn=MySQLdb.connect(host="221.228.228.4",user="root",passwd="uqcqa8zd",db="dsp_test")
    cursor = conn.cursor ()
    #打印多少条记录
    viewdata =  cursor.execute("SELECT * FROM  %d"  % view )
    
    #打印具体内容
    data = cursor.fetchmany(viewdata)
    return data
    #for i in info:
      #  mysqlsid =  i[0]
        #yield mysqlsid

    cursor.close ()
    conn.close ()

def main():
    get_view('virtual_baidu_solution_view')
    

if __name__ == '__main__':
    main()