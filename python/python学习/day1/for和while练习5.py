#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''
#for#
###1-1000的sum
su = 0
for i in range(1,1001):
    su += i
print su

###1-1000的偶数的sum
su1 = 0
for a in range(1,1001):
    if a%2 == 0:
        su1 += a
print su1

####while##
###1-1000的sum
su2 = 0
b = 0
while b < 1001:
    su2 = su2 +b
    b += 1
print su2

###1-1000的偶数的sum
su3 = 0
x = 0
while x < 1001:
    if x%2 == 0:
        #print x
        su3 = x + su3
    x += 1
print su3







