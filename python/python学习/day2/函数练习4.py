#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-10-25
@author: ymy
'''


def main():
    
      start = 1 
      end = 1001
      while True:
          
              current = (start + end) / 2

              i = raw_input('is number %d?' % current)
              if i == 'quit':
                  return
              elif i == 'big':
                 end = current 
              elif i == 'small':
                 start = current + 1
              elif i == 'eq':
                print current 
                return
#这个表示执行的是此代码所在的文件。 如果这个文件是作为模块被其他文件调用，不会执行这里面的代码。 只有执行这个文件时， if 里面的语句才会被执行。 这个功能经常可以用于进行测试。
if __name__ == '__main__': 
    main()