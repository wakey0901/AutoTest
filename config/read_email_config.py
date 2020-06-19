# coding:utf-8
import os
import configparser
# 读取邮件数据
# os.path.realpath(__file__)：返回当前文件的绝对路径
# os.path.dirname()： 返回（）所在目录
cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前文件的所在目录
configPath = os.path.join(cur_path, "email_config.ini")  # 路径拼接：/config/email_config.ini
conf = configparser.ConfigParser()
conf.read(configPath, encoding='UTF-8')  # 读取/config/email_config.ini 的内容

# get(section,option) 得到section中option的值，返回为string类型
smtp_server = conf.get("email", "smtp_server")
sender = conf.get("email", "sender")
user_name = conf.get("email","user_name")
password = conf.get("email", "password")
receiver = conf.get("email", "receiver")
port = conf.get("email", "port")
