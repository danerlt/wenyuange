#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: t_logutil.py 
@time: 2022-11-09
@contact: danerlt001@gmail.com
@desc: 
"""

from common.logger import logger, creater_logger

api_logger = creater_logger("api")
app_logger = logger
default_logger = creater_logger()

api_logger.info("aaaa")
app_logger.info("bbbb")
default_logger.info("ddddd")
