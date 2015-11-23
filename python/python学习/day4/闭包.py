#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''

def func2(f):
    def func3(x, y):
        print 'x is %d, y is %d' % (x, y)
        r = f(x, y)
        print 'result is %d'  %r
        return r

#@func2

def add(x, y):
    return x + y

print add(5, 7)

# def main():
#     test = add(5, 6)
#     print test
#     
# if __name__ == '__main__':
#     main()




def memorized(f):
    d = {}
    def inner(n):
        if n not in d:
            d[n] = f(n)
            return d[n]
        return inner
@memorized

def fib(n):
    if n < 1:return 1
    return fib(n-1) + fib(n-2)

def main():
    print map(fib, range(5000))

if __name__ == '__main__':
     main() 
    
    
    

