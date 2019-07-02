#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import textwrap

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: www.itdiffer.com')
        
class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input_word):
        #self.write(input_word[::-1])
        #把输入的内容转成数字并相加输出
        ipw = 0
        for i in input_word:
            ipw = ipw + int(i)
        self.write(str(ipw))

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(text, width))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler),
        (r"/reverse/(\w+)", ReverseHandler),
        (r"/wrap", WrapHandler)        
      ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


