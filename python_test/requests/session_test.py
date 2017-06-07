# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :使用requests的session类，可以伪造header信息
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:

import requests
import json
from requests import exceptions
URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    print json.dumps(json.loads(json_str),indent=4)

def fake_request():
    from requests import Session,Request
    sess  = Session()
    headers = {'User-agent':'this is a fake User-agent'}
    req = Request('GET',build_uri('user/emails'),auth=('1n4','678201yjy'),headers=headers)
    prep = req.prepare()
    print  "prep.body----->%s" % prep.body
    print  "prey.headers----->%s" % prep.headers

    resp = sess.send(prep)
    print "resp.status_code--->%s" % resp.status_code
    print "resp.headers--->%s" % resp.headers
    print "resp.request.headers--->%s"%resp.request.headers
    print "resp.text-->%s" % resp.text

if __name__ == '__main__':
    print "fake_request--->session test>>>>>>>'"
    fake_request()



