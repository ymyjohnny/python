#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年8月22日
@author:ymy
Copyright ymyjohnny@gmail.com
'''


import ftplib
import datetime
import zipfile
import os
import socket
#import tarfile
import zipfile

host = '14.18.155.218'
username = 'chuanyang'
password = 'Cy@Ftp201808'

hostname = socket.gethostname()

f = ftplib.FTP(host)
f.login(username, password)
#pwd_path = f.pwd()
#print("FTP当前路径:", pwd_path)

def ftp_upload(date,adx):
    file_remote = '%s_%s_requestlog_%s.zip' % (adx,date,hostname)
    #print file_remote
    biddir = "/data/algorithm/log/%s-bidder" % adx
    if os.path.exists(biddir):
      os.chdir(biddir)
      #print os.getcwd()
      file_local = 'request.log.%s'  % date
      #print file_local
      if os.path.exists(file_local):
        f1 = zipfile.ZipFile(file_remote, 'w', zipfile.ZIP_DEFLATED)
        f1.write(file_local)
        f1.close()
#        tf = tarfile.open(file_remote,"w:bz2")
#        tf.add(file_local) 
#        tf.close

        bufsize = 10240  # 设置缓冲器大小
        fp = open(file_remote, 'rb')
        f.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()
        os.remove(file_remote)
    

def main():
    d1 = datetime.datetime.now()
    d1.strftime("%Y-%m-%d_%H")
    d2 = d1 - datetime.timedelta(hours=1)
    date = d2.strftime("%Y-%m-%d-%H")
    adxes = ["taobao","baidu","youku","iqiyi","tencent","gdt","sohu","quantone","adinall"]
    for adx in adxes:
        ftp_upload(date,adx)
    f.quit()
if __name__ == '__main__':
    main()
