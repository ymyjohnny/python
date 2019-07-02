#!/usr/bin/python
#coding=utf-8
'''
Created on 2018年8月10日
@author:ymy
Copyright ymyjohnny@gmail.com
'''

import pexpect

child = pexpect.spawn('ssh root@10.21.10.119  ls')
f = file('testfile','w')
child.logfile = f

child.expect('password:')
child.sendline('point9*')sshp 
child.expect('$')
child.sendline('ls /home')
child.expect('$')

