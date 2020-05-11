# 快速启动该项目

你应该已经安装了Python 3.0 或更高的版本，这是必需的。

## 1. 安装和激活虚拟环境（可选步骤）

* Windows上：

```powershell
python -m venv <你希望创建虚拟环境的路径>
cd <你希望创建虚拟环境的路径>
.\Scripts\activate
cd ..\
```

* Linux/Mac OS上：

```bash
[sudo] apt-get install python3-venv
python -m venv <你希望创建虚拟环境的路径>
cd <你希望创建虚拟环境的路径>
source ./bin/activate
cd ../
```

## 2. 远程拉取仓库到本地

* （方法1）GitLab HTTPS：

```bash
git clone https://se.jisuanke.com/axy/api_app.git
```

* （方法2）GitLab SSH：

```bash
git clone git@se.jisuanke.com:axy/api_app.git
```

* （方法3）GitHub：

```bash
git clone https://github.com/aoxy/api_app.git
```

## 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 4. 启动项目

```bash
python .\app\api.py
```

---

如果输出类似下面这样的内容，就成功启动了该项目，可以测试`api`了。

```powershell
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
