#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-22
@author: ymy
'''


import unittest
import logging
from datetime import datetime
import  os

def filter_date(source):
    now = datetime.now()
    for filepath, st, dt in source:
        if dt.day == 1:
            logging.info('%s is ok.', filepath)
            continue
        if dt.weekday() == 0:
            logging.info('%s is ok.', filepath)
            continue
        if (now - dt).days <= 7:
            logging.info('%s is ok.', filepath)
            continue
        yield filepath

class TestDateFilter(unittest.TestCase):

  def test_date(self):
      source = [
          ('1', None, datetime(2000, 1, 1)),
          ('2', None, datetime(2000, 1, 2)),
          ('3', None, datetime(2000, 1, 3)),
          ('4', None, datetime.now()),
          ]
      self.assertEqual(list(filter_date(source)), ['2',])

if __name__ == '__main__':
    unittest.main()