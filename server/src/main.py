#!/usr/bin/env python
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: main.py 
@time: 2022-11-08
@contact: danerlt001@gmail.com
@desc: 
"""
import logging

import click

from common.app import app
from utils import logutil

logger = logging.getLogger(__name__)

cli = click.Group("文渊阁")


@cli.command("init")
@click.option("--config", "-c", default="./config/config.yaml", help="配置文件")
def init():
    """初始化"""
    pass


@cli.command("run")
@click.option("--config", "-c", default="./config/config.yaml", help="配置文件")
def run(config):
    """启动服务"""
    print(config)
    # app.run(host=host, port=port)


if __name__ == '__main__':
    cli()
