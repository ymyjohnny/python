#!/usr/bin/python
#coding=utf-8
'''
Created on 2016-10-27
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import smtplib
from email.mime.text import MIMEText
#mailto_list=['ymyjohnny@gmail.com','land_dai@adsame.com','qiqi_gu@adsame.com']           #收件人(列表)
mailto_list=['dsp_adsame@adsame.com']           #收件人(列表)
mail_host="smtp.adsame.com"            #使用的邮箱的smtp服务器地址
mail_user="report@adsame.com"                           #用户名
mail_pass="f9j3klE/[r"                             #密码
mail_postfix="adsame.com"                     #邮箱的后缀
def send_mail(to_list,sub,content):
    #me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    me="严旻元"+"<"+'report'+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain', _charset='utf-8')
    #msg = MIMEText(content,'utf8')
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
#f = open('mail.txt')
#for i in range(1):                             #发送5封，不过会被拦截的。。。
#    if send_mail(mailto_list,"",f.read()):  #邮件主题和邮件内容
#        print "done!"
#    else:
#        print "failed!"
#f.close()
