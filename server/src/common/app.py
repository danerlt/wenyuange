# !/usr/bin/env python
# -*- coding:utf-8 -*-  
""" 
@author: danerlt 
@file: app.py 
@time: 2022-11-09
@contact: danerlt001@gmail.com
@desc: 
"""

from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health():
    return "server is ok"


@app.get("/")
def index():
    return "This is wenyuange"
