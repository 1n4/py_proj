#coding:utf-8

from math import  sin,pow,log
import os
import logging

def f(x):
    print sin(x)
    print pow(x,2)
    print log(x,2)
    print logging.log(x,"this is a test")

f(30)

def fileCheck(file_path):
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            print   "its a directory"
        elif os. path.isfile(file_path):
            print "its a file"
        elif os.path.islink(file_path):
            print "its a link"
        else:
            print "unknow file"
    else:
        print "file or directory dose not exist"

fileCheck(r'c:\windows')
fileCheck(r'c:\windows\txt')

