import time
from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response, session

# 操作数据库
import database as db


app = Flask(__name__)
# 初始化，建表
db.initial()
# 用命令 python -c 'import os; print(os.urandom(24))' 生成
app.secret_key = '\xb9dLy\xbc\xe4\xd5D\x04s8\xfei\xf377i\x17~\x08_9)R'


@app.route('/user/signup/', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.args.get('username')
        password = request.args.get('password')
        if username is not None and password is not None and username != "" and password != "":
            message = db.insert(username, password)
        else:
            message = "请输入合法的用户名和密码！"
        return jsonify(msg=message, username=username, password=password)


if __name__ == '__main__':
    app.run()
