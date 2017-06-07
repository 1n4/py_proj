# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :requests库的见用法，获取和修改github用户信息
# **MODIFIED BY :     
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

def request_method():
    response = requests.get(build_uri('users/1n4'),timeout=10)
    print better_print(response.text)
    response2 = requests.get(build_uri('user/emails'),auth=('1n4','678201yjy'))
    print better_print(response2.text)


def  params_request():
    response = requests.get(build_uri('users'),params={'since':10})
    print better_print(response.text)
    print response.request.headers
    print response.url


def patch_request():
    response=requests.patch(build_uri('user'),auth=('1n4','678201yjy'),json={'name':'1n4y','email':'yinandyi@sina.com'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.url

def timeout_request():
    try:
        response = requests.get(build_uri('users/1n4'),timeout=0.1)

    except exceptions.Timeout as e:
        print e.message

    except exceptions.HTTPError as e:
        print e.message
    else:
        print better_print(response.text)
        response2=requests.get(build_uri('user/emails'),auth=('1n4','678201yjy'))
        print better_print(response2.text)


if __name__  ==  '__main__':
    print 'requset_method-->获取用户信息>>>>>>>'
    request_method()
    print 'params_request-->取10个id信息>>>>>'
    params_request()
    print 'patch_request-->修改用户名和邮箱>>>>>'
    patch_request()
    print "timeout_request-->测试异常获取>>>>>>"
    timeout_request()





