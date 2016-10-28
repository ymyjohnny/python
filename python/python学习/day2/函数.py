#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''

def abc(a,b,c):
    return c,b,a 
a,b,c = abc(1,2,3)
print a

#匿名函数
print (lambda a,b:a+b)(5,7)

##参数不固定用*
#写一个函数 计算输入多个值的和
def add(*l):
    s = 0
    for i in l:
        s += i 
    return s 
print add(1,2,3,4,5,6,7)


#reduce 迭代函数
def add1(x,y):
    return x+y
reduce(add1, range(1,3))



def add1(a,b,c):
    print a,b,c 
add(1,b=2,c=3)



l = [1,2,3,4,5]
def addn(n):
    return lambda x: x +n 













