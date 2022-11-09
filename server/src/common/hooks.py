#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author: danerlt 
@file: hooks.py 
@time: 2022-11-09
@contact: danerlt001@gmail.com
@desc: 
"""
import datetime
import json

from flask import request, jsonify

from common.app import app
from common.logger import creater_logger, logger

api_logger = creater_logger("api")


@app.before_request
def before_request():
    """每次请求接口之前处理
    """
    try:
        url = request.path

        # 忽略部分URL
        ignore_urls = ["/health"]
        for ignore_url in ignore_urls:
            if ignore_url in url:
                return

        method = request.method
        params = request.args
        data = request.data
        try:
            data = json.loads(data)
        except Exception as e:
            pass
        msg = f"开始HTTP {method} 请求, url: {url}, params: {params}, data: {data}"
        api_logger.info(msg)
        logger.info(msg)
    except Exception as e:
        msg = f"before_request error: {str(e)}"
        api_logger.warning(msg)
        logger.warning(msg)


@app.after_request
def after_request(response):
    """每次请求接口之前处理
    """
    try:
        url = request.path

        # 忽略部分URL
        ignore_urls = ["/health"]
        for ignore_url in ignore_urls:
            if ignore_url in url:
                return

        method = request.method
        params = request.args
        data = request.data
        try:
            data = json.loads(data)
        except Exception as e:
            pass

        # xss 漏洞 转义
        try:
            res_data = response.json
            msg = res_data.get("msg", "")
            msg = msg.replace('<', '&lt;')
            msg = msg.replace('>', '&gt;')
            # 数据库执行报错屏蔽掉
            pass_errors = ["pymssql", "pymysql", "sqlalchemy"]
            for pass_error in pass_errors:
                if pass_error in msg:
                    msg = "数据库执行SQL出错"
        except Exception as err:
            msgs = f"after_request msg处理error: {str(err)}"
            api_logger.warning(msgs)
            logger.warning(msgs)
        else:
            msgs = f"结束HTTP {method} 请求, url: {url}, params: {params}, data: {data},响应结果：{res_data}"
            api_logger.info(msgs)
            logger.info(msgs)
    except Exception as e:
        msgs = f"after_request error: {str(e)}"
        logger.warning(msgs)
        api_logger.warning(msgs)
    return response


@app.errorhandler(422)
def handle_param_error(err):
    """
    捕获422的异常码 参数错误
    :param err: 异常
    :return:
    """
    err_data = err.data
    api_logger.debug(f"handle_error 参数错误, err.data: {err_data}")
    messages = err_data.get("messages", {})
    api_logger.debug(f"handle_error messages: {messages}")

    msg = f"参数错误: "
    field_err_msgs = []
    for location, msg_dict in messages.items():
        for field_name, err_list in msg_dict.items():
            field_err_msg = " ".join(err_list)
            field_err_msg = field_err_msg.strip()
            field_err_msg = f"{field_name}: {field_err_msg}"
            field_err_msgs.append(field_err_msg)
    filed_err_msg = " ".join(field_err_msgs)
    msg += filed_err_msg
    result = {
        "code": 20000,
        "msg": msg,
        "logID": str(datetime.datetime.now()),
    }
    return jsonify(result)


@app.errorhandler(Exception)
def handle_exception(error):
    """
    处理接口返回异常的格式
    :param error: 异常
    :return:
    """
    if hasattr(error, 'code'):
        try:
            code = int(error.code)
        except Exception as e:
            code = 200
    else:
        code = 200
    api_logger.error(f"handle_g_exception error: {error}")
    # fix xss 漏洞 转义
    msg = str(error)
    msg = msg.replace('<', '&lt;')
    msg = msg.replace('>', '&gt;')
    # 数据库执行报错屏蔽掉
    pass_errors = ["pymssql", "pymysql", "sqlalchemy"]
    for pass_error in pass_errors:
        if pass_error in msg:
            msg = "数据库执行SQL出错"
    return json.dumps({"msg": msg, "status": 'error'}), code
