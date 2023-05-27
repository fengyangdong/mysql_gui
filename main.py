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


class Main:
    def __init__(self):
        with open("data\mysql.json", "r") as fp:
            self.data = json.load(fp)



class Student:
    def __init__(self):
        #
        qfile = QFile("data/ui/student.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.ui.information_widget.hide()

        self.slot()
    def slot(self):
        self.ui.student_information.clicked.connect(self.student_information)

    def student_information(self):
        self.ui.information_widget.show()
        data = sqls.select_student(login_ui.data_mysql, login_ui.data_user)
        self.ui.information_word.setText

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
        user_data = sqls.in_determine(self.data_mysql)
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

                        self.data_user["password"] = self.ui.user_password.text()
                        with open(r"data\user.json", "w") as fp:
                            json.dump(self.data_user, fp, ensure_ascii=False)
                    else:

                        self.data_user["password"] = ""
                        with open(r"data\user.json", "w") as fp:
                            json.dump(self.data_user, fp, ensure_ascii=False)
                    # 修改界面
                    self.ui.hide()
                    if user[2] == 3:
                        print("这是学生")
                        student_ui.ui.show()
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
        # 只要需要连接mysql，就需要更新一次数据库，以免用户中途修改数据库，但是注册的时候不用修改mysql.json，可以先修改data_mysql的值
        self.data_mysql["database"] = self.ui.user_database.text()
        register_ui.ui.show()


class Register:
    def __init__(self):
        #
        qfile = QFile("data/ui/register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.slot()

    def slot(self):
        self.ui.register_button.clicked.connect(self.fun_login)


    def fun_login(self):
        # 判断用户名是否重复
        user_data = sqls.in_determine(login_ui.data_mysql)
        for user in user_data:
            if self.ui.user_name.text() == user[0]:
                print("用户名不能重复")
                self.ui.register_word.setText("用户名不能重复")

                break
        else:
            user_id = sqls.select_student(login_ui.data_mysql, self.ui.user_id.text())
            for id in user_id:
                if id[0] == self.ui.user_id.text():
                    print("开始添加")
                    self.ui.register_word.setText("开始添加")
                    sqls.add_user(login_ui.data_mysql, self.ui.user_name.text(), self.ui.user_password.text(), 3, id[0])
                    self.ui.register_word.setText("开始添加-->添加完成")
            print(user_id)
            if int(user_id[0]) != 0:
                print("开始添加")
                self.ui.register_word.setText("开始添加")
                sqls.add_user(login_ui.data_mysql, self.ui.user_name.text(), self.ui.user_password.text(), 3)
                self.ui.register_word.setText("开始添加-->添加完成")
            else:
                self.ui.register_word.setText("没有")





app = QApplication(sys.argv)

login_ui = Login()

register_ui = Register()
student_ui = Student()
login_ui.ui.show()
sys.exit(app.exec_())

























