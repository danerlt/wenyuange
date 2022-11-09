#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt  
@file: const.py 
@time: 2022-08-12
@contact: danerlt001@gmail.com
@desc:  常量定义
"""

from pathlib import Path

# 时间正则表达式
RE_TIME = "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$"
# 时间格式 年-月-日 时:分:秒
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
# 日期格式 年-月-日
DATE_FORMAT = "%Y-%m-%d"

# 路径配置相关
current_path = Path(__file__)

COMMON_PATH = current_path.parent
# src目录路径
SRC_PATH = COMMON_PATH.parent

# 项目根路径
ROOT_PATH = SRC_PATH.parent

# config目录路径
CONFIG_PATH = SRC_PATH.joinpath("config")

# config.yaml 文件名 公共配置
CONFIG_FILE_NAME = "config.yaml"
# common.yaml路径
CONFIG_FILE_PATH = CONFIG_PATH.joinpath(CONFIG_FILE_NAME)
