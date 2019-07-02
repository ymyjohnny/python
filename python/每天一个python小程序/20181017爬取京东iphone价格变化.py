# -*- coding: utf-8 -*-
# @Author: ymy
# @Date:   2018-10-17 14:17:33
# @Last Modified by:   ymy
# @Last Modified time: 2018-10-17 16:07:14


import urllib2 
import json

import smtplib
import datetime
import os

from email.mime.text import MIMEText
mailto_list=['ymyjohnny@adsame.com']           #收件人(列表)
mail_host="smtp.adsame.com"            #使用的邮箱的smtp服务器地址
mail_user="report@adsame.com"                           #用户名
mail_pass="f9j3klE/[r"                             #密码
mail_postfix="adsame.com"                     #邮箱的后缀

def send_mail(to_list,sub,content):
    #me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    me="严旻元"+"<"+'report'+"@"+mail_postfix+">"
    #msg = MIMEText(content,_subtype='plain', _charset='utf-8')
    #msg = MIMEText(content,_subtype='html', _charset='utf-8')

    msg = MIMEText(content,'utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    try:
        #server = smtplib.SMTP()
        server = smtplib.SMTP_SSL(mail_host,465)
        #server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

from sendmail import *


def jd_price(url):
        sku = url.split('/')[-1].strip(".html")
        #print sku
        #以下url是京東生成價格的js
        price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku
        response = urllib2.urlopen(price_url)
        content = response.read()
        result = json.loads(content)
        #print result
        record = result[0]
        #print record['p']
        return record['p']  





if __name__=="__main__":
    f = open('/tmp/ipone_price','a')
    sub = '价格'
    try:
        jdprice = jd_price("https://item.jd.com/100000287117.html")
        if float(jdprice) < 11999:
            data = '价格请求成功,价格为%s' % str(jdprice)
            f.write(data)
    except:
        data1 = 'url 请求失败,无法获取价格'
        f.write(data1)
    f.close()

    f1 = open('/tmp/ipone_price','r')
    if len(f1.read()) != 0:
        f1.seek(0) #文件指针重新回到文件开头，重读文件
        if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
            print "done!"
        else:
             print "failed!"
    else:
      print "no data"
    f1.close()
    os.remove('/tmp/ipone_price')

