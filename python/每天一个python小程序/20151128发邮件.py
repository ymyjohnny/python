#! /usr/bin/env python  
#coding: utf-8 
import smtplib
from email.mime.text import MIMEText
mailto_list=['xxx@163.com']           #收件人(列表)
mail_host="mail.xxx.com"            #使用的邮箱的smtp服务器地址
mail_user="xxx"                           #用户名
mail_pass="xxx"                             #密码
mail_postfix="xxx.com"                     #邮箱的后缀
def send_mail(to_list,sub,content):
    #me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    me="hello"+"<"+'test'+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain', _charset='utf-8')
    #msg = MIMEText(content,'utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
f = open('mail.txt')
for i in range(1):                             #发送5封，不过会被拦截的。。。
    if send_mail(mailto_list,"测试中文",f.read()):  #邮件主题和邮件内容
        print "done!"
    else:
        print "failed!"
f.close()