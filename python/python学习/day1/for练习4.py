#coding=utf-8
'''
Created on 2015-10-24
@author: ymy
'''
#月球上你的体重是在地球上的16.5%，假设你每年增长1公斤，打印未来15年你的体重状况

# weight = 60
# Moonweight = weight*0.165
#  
# for i in range(1,16):
#     print (weight + i)*0.165

weight = 60       #体重
increment = 1       #体重年增量
coefficient = 0.165 #体重转换系数
 
for x in range(1, 16):
    print("%d years later: %0.2f" % (x, (weight + increment * x) * coefficient))

