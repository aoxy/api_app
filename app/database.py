import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def create_token(username):
    '''
    生成token
    :param username:用户名
    :return: token
    '''

    # 第一个参数是内部的私钥
    # 第二个参数是有效期(秒)
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    # 接收用户名、转换与编码
    token = s.dumps({"username": username}).decode("ascii")
    return token


def initial():
    '''
    初始化数据库，创建一个表user存用户名和加密过的密码
    '''
    try:
        with sql.connect("api.db") as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS user")
            cur.execute(
                "CREATE TABLE user(USERNAME varchar(32) PRIMARY KEY, ENC_PASSWORD varchar(128) NOT NULL)")
            con.commit()
    except BaseException:
        con.rollback()
    finally:
        con.close()


def insert(username, password):
    '''
    注册用户，用户名未占用的才能注册，把密码加密后再存入数据库
    '''
    try:
        with sql.connect("api.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO user(USERNAME, ENC_PASSWORD) VALUES(?, ?)",
                (username, generate_password_hash(password)))
            con.commit()
            msg = '注册成功！'
    except BaseException:
        con.rollback()
        msg = '该用户名已被占用，注册失败！'
    finally:
        con.close()
        return msg
