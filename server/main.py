#!/usr/bin/env python
# -*- coding:utf-8 -*-  
""" 
@author: danerlt
@file: main.py 
@time: 2022-11-08
@contact: danerlt001@gmail.com
@desc: 
"""

import uvicorn
from fastapi import FastAPI

# from common.app import app

app = FastAPI()

@app.get("/health")
def health():
    a = 1
    b = 2
    res = a / b
    print(res)
    return {"status": "ok", "msg": "health"}


@app.get("/")
def index():
    return "This is wenyuange"


def init():
    """初始化"""
    pass


def run():
    """启动服务"""
    uvicorn.run(app, host="0.0.0.0", port=8000)


def migrate():
    """数据库变更"""
    pass


def main():
    run()


if __name__ == '__main__':
    main()
