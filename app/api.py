import time
from flask import Flask, redirect, url_for, request, render_template, json, make_response, session

#操作数据库
import database as db
