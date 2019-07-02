#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:test.py

import os
#抓取环境变量

print "Content-type: text/html"
print
print "<meta charset=\"utf-8\">"
print "<b>环境变量</b><br>";
print "<ul>"
for key in os.environ.keys():
    print "<li><span style='color:green'>%s </span> : %s </li>" % (key,os.environ[key])
print "</ul>"
