import functools
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

import database as db


def create_token(username):
    '''
    生成token，返回token
    '''
    # 第一个参数是内部的私钥，第二个参数是有效期(秒)
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    # 接收用户名、转换与编码
    token = s.dumps({"username": username}).decode("ascii")
    return token


def verify_token(token):
    '''
    校验token，返回用户名
    '''
    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    username = db.query_login(data["username"])
    return username

