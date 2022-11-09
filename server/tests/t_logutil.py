#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: t_logutil.py 
@time: 2022-11-09
@contact: danerlt001@gmail.com
@desc: 
"""
import logging

from utils import logutil

api_logger = logging.getLogger("api")
app_logger = logging.getLogger("app")
default_logger = logging.getLogger()

api_logger.info("aaaa")
app_logger.info("bbbb")
default_logger.info("ddddd")
