# coding:utf-8
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser

# 读取DB配数据
# os.path.realpath(__file__)：返回当前文件的绝对路径
# os.path.dirname()： 返回（）所在目录
cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "db_config.ini")  # 路径拼接：/config/db_config.ini
conf = configparser.ConfigParser()
conf.read(configPath, encoding="UTF-8")

host = conf.get("mysqlconf", "host")
port = conf.get("mysqlconf", "port ")
user = conf.get("mysqlconf", "user")
password = conf.get("mysqlconf", "password")
port = conf.get("mysqlconf", "port")
