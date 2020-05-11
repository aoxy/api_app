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
