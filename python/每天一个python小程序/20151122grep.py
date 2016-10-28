#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-16
@author: ymy
'''

#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-11-16
@author: ymy
'''

import re



f1 = open('19505ext')
f = open('19505win')

def findString(fileObj, regex):
    for i in regex.splitlines():
        if not re.search(i, fileObj):
            print i


def main():
    findString(f.read(), f1.read())
    f.close()
    f1.close()
if __name__ == '__main__':
    main()
    