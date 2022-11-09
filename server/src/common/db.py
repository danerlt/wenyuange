#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt  
@file: db.py 
@time: 2022-08-11
@contact: danerlt001@gmail.com
@desc: 
"""
import logging
from flask_sqlalchemy import SQLAlchemy

from common import config
from common.app import app

logger = logging.getLogger()

db_uri = config.DATA_CONFIG.get("db_uri")
logger.info(f"db_uri: {db_uri}")
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 3600
}

debug = config.SERVER_CONFIG.get("debug")
logger.info(f"debug: {debug}, type: {type(debug)}")
app.config["SQLALCHEMY_ECHO"] = debug
db = SQLAlchemy(app, session_options={"autoflush": False})
