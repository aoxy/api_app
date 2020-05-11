import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, current_app

# 在实现基础功能
import utilit as ut


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


def query(username, password):
    try:
        with sql.connect("api.db") as con:
            cur = con.cursor()
            cursor = cur.execute("select * from user")
            con.commit()
    except BaseException:
        con.rollback()
    finally:
        for row in cursor:
            if check_password_hash(row[1], password) and username == row[0]:
                token = ut.create_token(username)
                con.close()
                msg = '登录成功！'
                return msg, token
        msg = '用户名或密码错误！'
        token = ''
        con.close()
        return msg, token
