#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-15
@author: ymy
'''


class D(object):
    
    def __init__(self):
        self.a = 'hello, world'
        
    def geta(self):
        return self.__a
    
    def seta(self, a):
        a = a.replace('hello', '你好')
        self.__a = a
    
    a = property(geta, seta)
    
d = D()
print d.a
d.a = 'hello ymy'
print d.a



class Rectangle(object):
  def __init__(self, width, heigth):
      self.width = width
      self.heigth = heigth
  def getArea(self):
      return self.width * self.heigth
  area = property(getArea, doc='area of the rectangle')
print Rectangle(300, 250)




