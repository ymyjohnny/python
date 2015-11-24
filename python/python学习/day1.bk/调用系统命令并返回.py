#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''


import subprocess    
print subprocess.check_output(["ls","-l","/home/ymy"])


import os 
print os.popen("ls -l /home/ymy").read()