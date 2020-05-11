import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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
