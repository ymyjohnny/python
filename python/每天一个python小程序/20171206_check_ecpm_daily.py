#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年12月6日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import MySQLdb
import datetime
import time
import socket,os
from sendmail import *

ts = int(time.time())
hostname = socket.gethostname()



def get_sid_info(adx,adtype,date,flowtype):
    date1 = date + ' 00:00:00'
    date2 = date + ' 23:59:00'
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="uqcqa8zd",db="dsp_backend")
    cursor = conn.cursor ()
    sql = "SELECT * FROM  (dsp_daily_solution_winnotice  w  left join (SELECT s.id AS solutionID,s.flow_type AS flow_type,a.ad_type AS ad_type FROM (dsp.dsp_solutions s left join dsp.ad_sizes a on (s.ad_size_id = a.id) ) ) info on (w.solutionid = info.solutionID)) where time >= '%s' and  time <= '%s' and ad_type = '%s' and adx = '%s' and flow_type = '%s'" % (date1,date2,adtype,adx,flowtype)
    #print sql
    cursor.execute(sql)
    info = cursor.fetchall()
    return  info

def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d %H:%M:%S")
    d2 = d1 - datetime.timedelta(days=1)
    date = d2.strftime("%Y-%m-%d")
    sub = "%s 各渠道平均cpm" % date

    #print date
    adtypes = {"FIXED":"硬广",
                            "CLIP":"视频",
                            "FEEDS":"信息流"}
    flowtypes = ["PC","Mobile-App","Mobile-Web"]
    adxes = ["taobao","baidu","google","youku","iqiyi","tencent","gdt","letv","sohu","quantone","adinall"]
    #print "adx","广告类型","平台","cpm单价"
    f = open('mail.txt','a')
    fw = "<div><table border><th>渠道</th><th>平台</th><th>广告类型</th><th>投放量</th><th>平均cpm</th>"
    for adtype,adtypeinfo  in adtypes.items():
        #print "    "
        #print adtypeinfo,adtype
        #print  "   "
        for adx  in adxes:
            for flowtype in flowtypes:
                sid_infos = get_sid_info(adx,adtype,date,flowtype)
                if not sid_infos:
                    continue
                impression_sum = 0
                price_sum = 0
                for i in sid_infos:
                    impression = i[4]
                    price = i[3]
                    #adtype = i[8]
                    flowtype = i[7]
                    impression_sum +=  impression
                    price_sum +=  price
                    cpm = str(round(price_sum / impression_sum * 1000 ,2))
                #print adx,adtypeinfo,flowtype,impression_sum,cpm
                fw += "<tr><td><div align=right> %s </div></td><td><div align=right> %s </div></td><td><div align=right>%s</div></td><td><div align=right>%s</div></td><td><div align=right>%s</div></td></tr>" % (adx,flowtype,adtypeinfo,impression_sum,cpm)
                #fw = "<tr><td>" + adx + "</td><td><div align=right>" + flowtype + "</div></td><td><div align=right>" + adtypeinfo + "</div></td><td><div align=right>" + cpm + "</div></td></tr>\n"
                #print fw
                #f.write(fw)
    fw += "</table></div>"
    f.write(fw)
    f.close()
    f1 = open('mail.txt','r')
    if len(f1.read()) != 0:
        f1.seek(0) #文件指针重新回到文件开头，重读文件
        if send_mail(mailto_list,sub,f1.read()):  #邮件主题和邮件内容
            print "done!"
        else:
             print "failed!"
    else:
      print "no data"
    f1.close()
    os.remove('mail.txt')

                

if __name__ == '__main__':
    main()
