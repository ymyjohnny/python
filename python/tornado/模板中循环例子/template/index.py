#! /usr/bin/env python
#-*- coding:utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        lst = ["python","www.adsame.com","ymyjohnny@gmail.com"]  #定义一个list
        self.render("index.html", info=lst)                     #将上述定义的list传给模板

handlers = [(r"/", IndexHandler),]

#template_path = os.path.join(os.path.dirname(__file__), "temploop")  #模板路径
template_path = os.path.join(os.getcwd(), "template")  #模板路径
print template_path

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers,template_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()