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


class Login:
    def __init__(self):
        # 
        qfile = QFile("data/ui/login.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


        with open(r"data\user.json", "r") as fp:
            self.data = json.load(fp)
            data = self.data
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
    def slot(self):
        self.ui.user_in.clicked.connect(self.fun_in)
        self.ui.user_database_button.clicked.connect(self.fun_database)
    def fun_in(self):
        # 判断是否正确



        # 更新user.json的信息
        # 修改用户名和数据库
        self.data["username"] = self.ui.user_name.text()
        self.data["database"] = self.ui.user_database.text()
        with open(r"data\user.json", "w") as fp:
            json.dump(self.data, fp, ensure_ascii=False)
        # 修改密码部分
        if self.ui.user_radio.isChecked() == True:
            if self.data["password"] == "":
                self.data["password"] = self.ui.user_password.text()
                with open(r"data\user.json", "w") as fp:
                    json.dump(self.data, fp, ensure_ascii=False)
        else:
            if self.data["password"] != "":
                self.data["password"] = ""
                with open(r"data\user.json", "w") as fp:
                    json.dump(self.data, fp, ensure_ascii=False)

    def fun_database(self):
        if self.ui.user_database.text() in ("information_schema", "mysql", "performance__schema", "sys"):
            self.ui.user_word.setText("不能使用系统数据库")
        else:
            if self.temp_database ==  True:
                print("初始化")
                self.ui.user_word.setText("开始初始化")
                import sqls
                sqls.InitializeDatabase(self.ui.user_database.text())
                self.ui.user_word.setText("初始化完成")
            else:
                self.ui.user_word.setText("初始化数据库会删除之前数据库然后重建\n继续请在此点击")
                self.temp_database = True





















