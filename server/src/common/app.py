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

from common.json_encoder import OtherEncoder

app = Flask(__name__)
# 自定义json_decoder
app.json_encoder = OtherEncoder


@app.get("/health")
def health():
    return "server is ok"


@app.get("/")
def index():
    return "This is wenyuange"
