#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt  
@file: config.py 
@time: 2022-08-10
@contact: danerlt001@gmail.com
@desc: 读取配置文件，初始化项目相关配置
"""

import yaml

from common.const import CONFIG_FILE_PATH


def get_config(path, name=None):
    with open(path, "r", encoding="utf-8") as f:
        yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
        if name:
            cfg = yaml_dict.get(name)
            if cfg is None:
                raise Exception(f"获取{name}配置失败，配置不存在")
            return cfg
        else:
            return yaml_dict


SERVER_CONFIG = {}
DATA_CONFIG = {}
LOGGER_CONFIG = {}


def load_config_by_path(path: str):
    """从配置文件中重新加载配置

    :param path:
    :return:
    """
    try:
        global SERVER_CONFIG
        global DATA_CONFIG
        global LOGGER_CONFIG
        SERVER_CONFIG = get_config(path, "server")
        DATA_CONFIG = get_config(path, "data")
        LOGGER_CONFIG = get_config(path, "logger")
    except Exception as e:
        print(f"load_config_by_path error: {e}")


load_config_by_path(CONFIG_FILE_PATH)
