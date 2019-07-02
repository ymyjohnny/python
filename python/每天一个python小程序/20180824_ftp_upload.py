#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年8月24日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import ftplib
import os
import datetime
import zipfile

host = '14.18.155.218'
username = 'chuanyang'
password = 'Cy@Ftp201808'


f = ftplib.FTP(host)
f.login(username, password)

def ftp_upload(date):
    #传输文件名
    file_remote = '传到服务端的文件名' 
    #print file_remote
    filedir = "传输文件所在目录" 
    if os.path.exists(filedir):
        os.chdir(filedir)
        file_local = '本地需要传输的文件名'
        #print file_local
        if os.path.exists(file_local):
            f1 = zipfile.ZipFile(file_remote, 'w', zipfile.ZIP_DEFLATED)
            f1.write(file_local)
            f1.close()
            bufsize = 10240  # 设置缓冲器大小
            fp = open(file_local, 'rb')
            f.storbinary('STOR ' + file_remote, fp, bufsize)
            fp.close()
            #确认传输完成后可以删除,下面的remove注释打开
            os.remove(file_local)
            os.remove(file_remote)
    
def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d")
    d2 = d1 - datetime.timedelta(days=2)
    date = d2.strftime("%Y-%m-%d")
    ftp_upload(date)

if __name__ == '__main__':
    main()

