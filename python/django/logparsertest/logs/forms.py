#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-01-07
@author: Shell.Xu
@copyright: 2016, Shell.Xu <shell909090@gmail.com>
@license: cc
'''
from django import forms

class UploadFileForm(forms.Form):
    logfile = forms.FileField(label='upload')

