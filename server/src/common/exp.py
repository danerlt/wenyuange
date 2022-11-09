#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt  
@file: exp.py 
@time: 2022-08-12
@contact: danerlt001@gmail.com
@desc: 异常定义
"""


class MyBaseException(Exception):
    def __init__(self, msg):
        self.msg = str(msg)

    def __str__(self):
        return "ERROR: " + self.msg
