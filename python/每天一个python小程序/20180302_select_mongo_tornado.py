#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年3月2日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import json

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


def mongo_connection_show(select_db,select_table,select_id,date):
    client=pymongo.MongoClient("221.228.90.4",27018)
    print select_db
    db=client[select_db]
    conn=db[select_table]
    id = int(select_id)
    print id
    print db
    rows = conn.find({"id": id,"date":date}).limit(10)
    #rows = conn.find().limit(10)
    l = []
    for row in rows:
        print row
        try: 
            #删除mongo里的_id字段,无法被json解析
            del row["_id"]
            print row
            l.append(row)
        except:
            continue
    return l


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")
        #self.redirect('http://www.baidu.com')
           
class Dsp_MongoHandler(tornado.web.RequestHandler):
    def get(self):
        select_db = self.get_argument("select_db",{})
        select_table = self.get_argument("select_table",{})
        select_id = self.get_argument("select_id",{})
        print select_db
        print select_id
        date = self.get_argument("date",{})
        response = mongo_connection_show(select_db,select_table,select_id,date)
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        for i in response:
            self.write(json.dumps(i, ensure_ascii=False))
            #self.write(i)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler),(r"/dsp_mongos/", Dsp_MongoHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
