#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''


#写一个判断，分析一篇文章中有多少句话以“但是”开头。内容可以随便在网络上找一篇小说。
#小说目录 /home/ymy/python/uplooking/少年pi的奇幻漂流 中文版.txt

import os

txt = os.popen('cat /home/ymy/python/uplooking/少年pi的奇幻漂流\ 中文版.txt').read().decode('utf-8')
#print txt
su1 = 0
for i in txt.splitlines():
          #print i 
          for a in i.split(u"，"):
                for b in a.split(u"。"):
                   # for c in b.strip():
                    if b.startswith(u"但是"):
                        b = b.strip()
                        print b
                        su1 = su1+1
print su1

# for i in txt.split("，"):u
#    if i.startswith(" ") == True :
#         continue
#    elif  i.startswith("但是") == True:
#          su1 = a.append(i)[-1]
#          print su1
#        print  i.startswith("但是")
#        print i
#         

# for a in txt.split("。"):
#     if a.startswith("但是") == True:
#         print a


##########正确答案