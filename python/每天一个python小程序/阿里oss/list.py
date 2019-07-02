# -*- coding: utf-8 -*-

import os
import string
import re
import oss2


# 以杭州区域为例，Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'MfDlVdvHMWvlv2Y4')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'Knwz1UREUU85SthycvRZpcmkVBeTRc')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'adceshi')
#endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-beijing-mtrh-d01-a.ops.data.cctv.com/adceshi')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing-mtrh-d01-a.ops.data.cctv.com')

# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param


# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

#列出oss内容
dirlist = []
print "============目录文件内容=============="
date = '2018-12-26'
for i, object_info in enumerate(oss2.ObjectIterator(bucket)):
        dirlist.append(format(object_info.key))
print dirlist

#官方示例
#for i, object_info in enumerate(oss2.ObjectIterator(bucket)):
#    print("{0} {1}".format(object_info.last_modified, object_info.key))
