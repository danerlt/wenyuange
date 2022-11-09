#!/usr/bin/env python
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: main.py 
@time: 2022-11-08
@contact: danerlt001@gmail.com
@desc: 
"""

import click

from common import config as cfg
from common.app import app
from common.config import load_config_by_path
from common.logger import logger

cli = click.Group("文渊阁")


@cli.command("init")
@click.option("--config", "-c", default="./config/config.yaml", show_default=True, help="配置文件")
def init(config):
    """初始化"""
    load_config_by_path(config)
    logger.info("初始化")


@cli.command("run")
@click.option("--config", "-c", default="./config/config.yaml", show_default=True, help="配置文件")
def run(config):
    """启动服务"""
    load_config_by_path(config)
    host = cfg.SERVER_CONFIG.get("host")
    port = cfg.SERVER_CONFIG.get("port")
    debug = cfg.SERVER_CONFIG.get("debug")
    logger.info("启动服务")
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    cli()
