import sys
import time
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PyQt5 import QtCore, QtGui, QtWidgets
from fuzzywuzzy import fuzz
import json
import os
from random import randint
from datetime import datetime, timedelta
from uuid import uuid4 as uid
import socket

import sqls
class Login:
    def __init__(self):
        #
        qfile = QFile("data/ui/login.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


        with open(r"data\user.json", "r") as fp:
            self.data_user = json.load(fp)
            data = self.data_user
        with open(r"data\mysql.json", "r") as fp:
            self.data_mysql = json.load(fp)
        print(type(data["username"]))
        self.ui.user_name.setText(data["username"])
        self.ui.user_password.setText(data["password"])
        self.ui.user_database.setText(data["database"])

        if data["password"] == "":
            self.ui.user_radio.setChecked(False)
        else:
            self.ui.user_radio.setChecked(True)
        self.temp_database = False
        self.slot()
        print(self.ui.user_database.text())
        print(self.ui.user_password.text())
        # print(self.ui.user_name.test())


    # 槽处理
    def slot(self):
        self.ui.user_in.clicked.connect(self.fun_in)
        self.ui.user_database_button.clicked.connect(self.fun_database)
        self.ui.user_logon.clicked.connect(self.fun_login)
    def fun_in(self):
        # 首先必须更新mysql.json的信息，因为这个是连接mysql的文件内容，而且前面初始化也没有修改mysql.json
        # 里面的信息，所以必须先修改mysql.json的信息
        # 更新mysql.json的信息
        self.data_mysql["database"] = self.ui.user_database.text()
        with open(r"data\mysql.json", "w") as fp:
            json.dump(self.data_mysql, fp, ensure_ascii=False)
        # 获取指定库的user表（导出的是元祖）
        user_data = sqls.select_user(self.data_mysql)
        # 遍历user表数据，挨个挨个判断
        for user in user_data:
            if self.ui.user_name.text() == user[0]:
                if self.ui.user_password.text() == user[1]:
                    print("登陆成功")
                    # 登录成功后，需要把登录的用户名和密码保存与否给处理一下
                    # 更新user.json的信息
                    # 修改用户名和数据库
                    self.data_user["username"] = self.ui.user_name.text()
                    self.data_user["database"] = self.ui.user_database.text()

                    with open(r"data\user.json", "w") as fp:
                        json.dump(self.data_user, fp, ensure_ascii=False)
                    # 修改密码部分
                    if self.ui.user_radio.isChecked() == True:
                        if self.data_user["password"] == "":
                            self.data_user["password"] = self.ui.user_password.text()
                            with open(r"data\user.json", "w") as fp:
                                json.dump(self.data_user, fp, ensure_ascii=False)
                    else:
                        if self.data_user["password"] != "":
                            self.data_user["password"] = ""
                            with open(r"data\user.json", "w") as fp:
                                json.dump(self.data_user, fp, ensure_ascii=False)
                    # 修改界面

                    break
                else:
                    print("密码错误")
                    break
        else:
            print("没有用户名")


    # 库初始化操作
    def fun_database(self):
        # 首先，不能是系统自带的数据库
        if self.ui.user_database.text() in ("information_schema", "mysql", "performance__schema", "sys"):
            self.ui.user_word.setText("不能使用系统数据库")
        else:
            if self.temp_database ==  True:
                print("初始化")
                self.ui.user_word.setText("开始初始化")
                # 开始初始化
                sqls.InitializeDatabase(self.data_mysql, self.ui.user_database.text())
                self.ui.user_word.setText("初始化完成")
            else:
                # 做一个提醒，需要在此点击按钮才行
                self.ui.user_word.setText("初始化数据库会删除之前数据库然后重建\n继续请在此点击")
                self.temp_database = True


    def fun_login(self):
        pass




















