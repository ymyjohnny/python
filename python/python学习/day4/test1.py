#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''
# def memorized(f):
#     d = {}
#     def inner(n):
#         if n not in d:
#             d[n] = f(n)
#             return d[n]
#         return inner
# @memorized
# def fib(n):
#     if n < 1:return 1
#     return fib(n-1) + fib(n-2)
# 
# def main():
#     print map(fib, range(5000))
# 
# if __name__ == '__main__':
#      main() 
     
def fib(n):
    if n < 1:return 1
    return fib(n-1) + fib(n-2)

def main():
    print map(fib, range(20))

if __name__ == '__main__':
     main() 