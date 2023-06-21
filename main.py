import sys
import time
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Signal, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from fuzzywuzzy import fuzz
import json
import os
from random import randint
from datetime import datetime, timedelta
from uuid import uuid4 as uid
import socket
import sqls
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys
all_header_checkbox = []
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
        #self.ui.label_title.setText(f"你好学生，您的编号是{login_ui.data_user['username']}")

        self.slot()
        self.hide()
    def slot(self):
        self.ui.student_information.clicked.connect(self.student_information)
        self.ui.change_information_button.clicked.connect(self.change_information)
        self.ui.change_button2.clicked.connect(self.change_information2)

    def hide(self):
        self.ui.information_widget.hide()
        self.ui.change_information.hide()

    def student_information(self):
        self.ui.information_widget.show()
        # data = sqls.select_one_student(login_ui.data_mysql, login_ui.data_user['username'])
        data = sqls.select_one_student(mysql_word=login_ui.data_mysql, id=login_ui.data_user['username'])
        student_data = f"""
        您的学号是：{data[0][0]}\n
        您的名称是：{data[0][1]}\n
        您的性别：{data[0][2]}\n
        您的电话：{data[0][3]}\n
        您的邮箱：{data[0][4]}\n
        您的家庭住址：{data[0][5]}\n
        您的寝室号：{data[0][6]}\n
        所在院：{data[0][7]}\n
        所在班：{data[0][8]}\n
        """
        self.ui.information_word.setText(student_data)

    def change_information(self):
        self.ui.change_information.show()
        data = sqls.select_one_student(mysql_word=login_ui.data_mysql,id=login_ui.data_user['username'])
        self.ui.change_user.setText(data[0][1])
        self.ui.change_sex.setText(data[0][2])
        self.ui.change_phone.setText(data[0][3])
        self.ui.change_email.setText(data[0][4])
        self.ui.change_home.setText(data[0][5])

    def change_information2(self):
        print("开始")
        sqls.change_student(login_ui.data_mysql, login_ui.data_user,self.ui.change_user.text(),\
                        self.ui.change_sex.text(),self.ui.change_phone.text(),self.ui.change_email.text(),\
                            self.ui.change_home.text())
        print("结束")
        self.student_information()



class Login:
    def __init__(self):
        # 加载qfile文件
        qfile = QFile("data/ui/login.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        # 获取需要的数据
        """
        其中user数据是登录界面默认输出数据
        mysql表是连接数据
        """
        with open(r"data\user.json", "r") as fp:
            self.data_user = json.load(fp)
            data = self.data_user
        with open(r"data\mysql.json", "r") as fp:
            self.data_mysql = json.load(fp)
        print(type(data["username"]))
        self.ui.user_name.setText(data["username"])
        self.ui.user_password.setText(data["password"])
        self.ui.user_database.setText(data["database"])
        # 如果password为空，那么就是上次登录的时候，取消了记住密码的选项
        if data["password"] == "":
            self.ui.user_radio.setChecked(False)
        else:
            self.ui.user_radio.setChecked(True)
        # 定义一个变量，后面初始化库会用到
        self.temp_database = False
        self.slot()


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
            # 如果输入的用户名和密码都正确，就登陆成功
            if self.ui.user_name.text() == user[0]:
                if self.ui.user_password.text() == user[1]:
                    print("登陆成功")
                    # 登录成功后，需要把登录的用户名和密码保存与否给处理一下
                    # 更新user.json的信息
                    # 修改用户名和数据库（主要是用于下次登录）
                    self.data_user["username"] = self.ui.user_name.text()
                    self.data_user["database"] = self.ui.user_database.text()

                    with open(r"data\user.json", "w") as fp:
                        json.dump(self.data_user, fp, ensure_ascii=False)
                    # 修改密码部分（如果保存密码就把密码保存进入，如果没有选择保存密码就保存空白）
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
                    if len(user[0]) == 6:
                        print("这是学生")
                        student_ui.ui.show()
                        student_ui.ui.label_title.setText(f"你好学生，您的编号是{login_ui.data_user['username']}")

                        break
                    elif len(user[0]) == 5:
                        print("这是老师")
                        break
                    elif len(user[0]) == 4:
                        sdept_ui.ui.show()
                        sdept_ui.ui.label_title.setText(f"你好院长，您的编号是{login_ui.data_user['username']}")
                        print("这是院长")
                        break
                    else:
                        print("这是root")
                        root_ui.ui.show()
                        break
                # 这里是用户名正确但是密码不正确
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
        #加载
        qfile = QFile("data/ui/register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.slot()

    def slot(self):
        self.ui.register_button.clicked.connect(self.fun_login)


    def fun_login(self):
        # 判断用户名是否重复
        user_data = sqls.select_user(login_ui.data_mysql)
        # 这里面只能是学生才能登录，所以id一定是6位，所以第一步就是判断id位数
        if len(self.ui.user_name.text()) == 6:
            # 开始判断
            for user in user_data:
                if self.ui.user_name.text() == user[0]:
                    print("用户名不能重复")
                    self.ui.register_word.setText("用户名不能重复")
                    break
            # 如果for循环顺利退出，就说明没有用户名重复，就可以进行检查学号是否正确
            else:
                user_id = sqls.select_one_student(mysql_word=login_ui.data_mysql, id=self.ui.user_name.text())
                if int(user_id[0][0]) != 0:
                    print("开始添加")
                    self.ui.register_word.setText("开始添加")
                    sqls.add_user(login_ui.data_mysql, self.ui.user_name.text(), self.ui.user_password.text())
                    self.ui.register_word.setText("开始添加-->添加完成")
                else:
                    self.ui.register_word.setText("没有")
        else:
            self.ui.register_word.setText("学号是6位，如果你不是学生请退出，学号错误")


class Root:
    def __init__(self):
        #加载
        qfile = QFile("data/ui/root.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        # slot处理
        self.slot()
        # 空白处理
        self.hide()
        # 初始化
        # 初始化title
        self.ui.root_title.setText(f"你是超级管理员，你的编号为{login_ui.data_user['username']}")
        # 初始化check操作
        header1 = CheckBoxHeader()
        self.ui.sdept_table.setHorizontalHeader(header1)  # 设置头复选框
        header1.select_all_clicked.connect(header1.change_state)  # 行表头复选框单击信号与槽
        self.ui.sdept_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.sdept_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        header2 = CheckBoxHeader()
        self.ui.user_table.setHorizontalHeader(header2)
        header2.select_all_clicked.connect(header2.change_state)  # 行表头复选框单击信号与槽
        self.ui.user_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        header3 = CheckBoxHeader()
        self.ui.student_table.setHorizontalHeader(header3)
        header3.select_all_clicked.connect(header3.change_state)  # 行表头复选框单击信号与槽
        self.ui.student_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.student_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        header4 = CheckBoxHeader()
        self.ui.class_table.setHorizontalHeader(header4)
        header4.select_all_clicked.connect(header4.change_state)  # 行表头复选框单击信号与槽
        self.ui.class_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.class_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        header5 = CheckBoxHeader()
        self.ui.course_table.setHorizontalHeader(header5)
        header5.select_all_clicked.connect(header5.change_state)  # 行表头复选框单击信号与槽
        self.ui.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.course_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def hide(self):
        self.ui.stackedWidget.hide()
        # self.ui.select_sdept.hide()
        self.ui.add_sdept.hide()
        self.ui.delete_sdept.hide()
        # self.ui.select_user.hide()
        self.ui.delete_user_widget.hide()
        self.ui.add_root_widget.hide()
        self.ui.change_password_widget.hide()
        self.ui.change_username_widget.hide()
    def slot(self):
        # sdept
        self.ui.all_sdept_button.clicked.connect(self.all_sdept)
        self.ui.add_sdept_button.clicked.connect(self.add_sdept)
        self.ui.add_sdept_button2.clicked.connect(self.add_sdept2)
        self.ui.delete_sdept_button.clicked.connect(self.delete_sdept)
        self.ui.delete_sdept_button2.clicked.connect(self.delete_sdept2)
        self.ui.add_user_button.clicked.connect(self.add_sdept_user)


        # user
        self.ui.all_user_button.clicked.connect(self.all_user)
        self.ui.delete_user.clicked.connect(self.delete_user)
        self.ui.delete_user2.clicked.connect(self.delete_user2)
        self.ui.add_root_button.clicked.connect(self.add_root)
        self.ui.add_root_button2.clicked.connect(self.add_root2)

        # student
        self.ui.all_student_button.clicked.connect(self.all_student)

        # teacher
        self.ui.all_teacher_button.clicked.connect(self.all_teacher)
        # class
        self.ui.all_class_button.clicked.connect(self.all_class)

        # course
        self.ui.all_course_button.clicked.connect(self.all_course)

        # 其他
        self.ui.exit_button.clicked.connect(self.exit)
        self.ui.word_help_button.clicked.connect(self.word_help)
        self.ui.my_word_button.clicked.connect(self.my_word)
        self.ui.change_password_button.clicked.connect(self.change_my_password)
        self.ui.change_password_button2.clicked.connect(self.change_my_password2)
        self.ui.change_username_button.clicked.connect(self.change_my_username)
        self.ui.change_username_button2.clicked.connect(self.change_my_username2)
    def all_sdept(self):
        """
        显示sdept的table，并且可以进行管理
        """
        # self.hide()
        # self.ui.select_sdept.show()
        # index0为学院管理
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(0)
        # 查询出所有目前有的学院
        sdept_tuple = sqls.select_sdept(mysql_word=login_ui.data_mysql)
        # 设置表格高度
        self.ui.sdept_table.setRowCount(len(sdept_tuple))
        # 加数据
        for row in range(0,len(sdept_tuple)):
            for column in range(0,len(sdept_tuple[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.sdept_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.sdept_table.setItem(row, column+1, QTableWidgetItem(f"{sdept_tuple[row][column]}"))


    def add_sdept(self):
        # 添加操作和删除操作是一起的，所以必须只能显示一个
        self.ui.add_sdept.show()
        self.ui.delete_sdept.hide()



    def add_sdept2(self):
        # TODO 待办 验证操作的完善
        # 添加操作需要验证，第一个，id不能相同，名称不能相同，第二个，老师id必须存在，第三个，sdept长度必须为4

        # 判断操作
        print(login_ui.data_mysql, self.ui.add_sdept_id.text(), self.ui.add_sdept_name.text(),
              self.ui.add_sdept_username.text())
        sqls.add_sdept(login_ui.data_mysql, self.ui.add_sdept_id.text(), self.ui.add_sdept_name.text(),self.ui.add_sdept_username.text())

        self.ui.label_word.setText("添加完成")
        # 更新table数据
        self.all_sdept()

    def delete_sdept(self):
        # 添加操作的界面隐藏，把删除界面显示
        self.ui.add_sdept.hide()
        self.ui.delete_sdept.show()

    def delete_sdept2(self):
        # TODO 待办 删除的同时删除user里面的数据
        # 判断那些行选中
        delete_list = []
        for row in range(self.ui.sdept_table.rowCount()):
            if self.ui.sdept_table.cellWidget(row, 0).isChecked() is True:
                # 把选中的行进行删除操作
                delete_list.append(self.ui.sdept_table.item(row,1).text())
        for id in delete_list:

            sqls.delete_sdept(login_ui.data_mysql,id)
        # 删除完，把表进行更新，这个就是
        self.all_sdept()

    def add_sdept_user(self):
        # 查询数据
        user_list = []
        sdept_list = []
        user_id = sqls.select_user(login_ui.data_mysql)
        for i in user_id:
            user_list.append(i[0])
        sdept_id = sqls.select_sdept(mysql_word=login_ui.data_mysql)
        for i in sdept_id:
            sdept_list.append(i[0])
        # 选择没有创建user的sdept
        print(user_list,sdept_list)
        for sdept in sdept_list:
            if sdept not in user_list:
                sqls.add_user(login_ui.data_mysql,sdept,123456)
        self.ui.label_word.setText("用户添加完成，默认账号为id，默认密码为123456")

    def all_user(self):
        # self.hide()
        # self.ui.select_user.show()
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(1)
        user_tuple = sqls.select_user(login_ui.data_mysql)
        self.ui.user_table.setRowCount(len(user_tuple))
        print(user_tuple)
        for row in range(0, len(user_tuple)):
            for column in range(0, len(user_tuple[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.user_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.user_table.setItem(row, column + 1, QTableWidgetItem(f"{user_tuple[row][column]}"))

    def delete_user(self):
        self.ui.delete_user_widget.show()

    def delete_user2(self):

        # 判断那些行选中
        delete_list = []
        for row in range(self.ui.user_table.rowCount()):
            if self.ui.user_table.cellWidget(row, 0).isChecked() is True:
                # 把选中的行进行删除操作
                delete_list.append(self.ui.user_table.item(row,1).text())
        for id in delete_list:
            sqls.delete_user(login_ui.data_mysql,id)
            print("操作完成")
        # 删除完，把表进行更新，这个就是
        self.all_user()

    def add_root(self):
        # TODO 去重
        self.ui.add_root_widget.show()

    def add_root2(self):
        # 把root的名称赋值给root_user
        root_user = self.ui.root_user.text()
        all_user = sqls.select_user(login_ui.data_mysql)
        # 不能使用4位5位6位号码
        if len(root_user) in (4,5,6):
            self.ui.label_word.setText("错误，用户名不能使用4位5位6位号码")
        else:
            # 不能是重复的
            for row in all_user:
                if row[0] == root_user:
                    self.ui.label_word.setText("错误，使用了相同的user，请修改名称")
                    break
            else:
                # 到这一步说明没有重复的，开始执行
                sqls.add_user(login_ui.data_mysql,root_user,"123456")
                self.ui.label_word.setText("添加成功")
                # 添加完成，更新table
                self.all_user()


    def all_student(self):
        # TODO 添加操作，需要修改
        # TODO 检索查询，删除学生操作，修改操作
        # 展示页面
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(2)


        # data = sqls.select_sdept(mysql_word=login_ui.data_mysql, id=login_ui.data_user["username"])
        # data = data[0][1]
        # print(data)
        # 查询这个院有什么班，依次加到box中
        # data_class = sqls.select_class(mysql_word=login_ui.data_mysql, sdept_name=data)
        # for c in data_class:
        #     self.ui.select_class_box.addItem(c[0])


        # 查询所有学生
        data = sqls.select_one_student(mysql_word=login_ui.data_mysql)
        print(data)
        self.ui.student_table.setRowCount(len(data))
        for row in range(0, len(data)):
            for column in range(0, len(data[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.student_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.student_table.setItem(row, column + 1, QTableWidgetItem(f"{data[row][column]}"))



    def all_class(self):
        # TODO 需要的功能和上面一样
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(3)
        # 查询所有班级信息
        data = sqls.select_class(mysql_word=login_ui.data_mysql)
        print(data)
        self.ui.class_table.setRowCount(len(data))
        for row in range(0, len(data)):
            for column in range(0, len(data[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.class_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.class_table.setItem(row, column + 1, QTableWidgetItem(f"{data[row][column]}"))

    def all_course(self):
        # TODO 需要的功能和上面一样
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(4)
        # 查询所有班级信息
        data = sqls.select_course(mysql_word=login_ui.data_mysql)
        print(data)
        self.ui.course_table.setRowCount(len(data))
        for row in range(0, len(data)):
            for column in range(0, len(data[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.course_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.course_table.setItem(row, column + 1, QTableWidgetItem(f"{data[row][column]}"))

    def exit(self):
        self.ui.hide()
        # 退出需要关闭堆栈的widget
        self.ui.stackedWidget.hide()
        # 退出还需要重新执行一次hide函数
        self.hide()
        login_ui.ui.show()


    def word_help(self):
        # 显示
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(5)

    def my_word(self):
        # 显示
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(6)
        data = sqls.select_user(login_ui.data_mysql, name=login_ui.data_user["username"])
        self.ui.my_word_label.setText(f"用户名：\t{data[0][0]}\n密码：   \t{data[0][1]}\n")
        self.ui.label_word.setText("修改用户名和密码的时候，都需要重新登录一次")

    def change_my_password(self):
        self.ui.change_password_widget.show()

    def change_my_password2(self):
        # 得到数据
        data = sqls.select_user(login_ui.data_mysql, name=login_ui.data_user["username"])
        data_username = data[0][0]
        data_password = data[0][1]
        # 两次密码需要输入正确一致
        if self.ui.new_password.text() == self.ui.new_password2.text():
            # 输入密码不能和之前的密码一致
            if data_password != self.ui.new_password.text():
               sqls.delete_user(login_ui.data_mysql, data_username)
               sqls.add_user(login_ui.data_mysql, data_username, self.ui.new_password.text())
               self.ui.label_word.setText("修改完成，注意：重新登录需要重新输入密码")
               # 退出登录，重新登录
               self.exit()
            else:
               self.ui.label_word.setText("旧密码和新密码一致，不能修改")

        else:
            self.ui.label_word.setText("你输入的密码前后不一致")

    def change_my_username(self):
        self.ui.change_username_widget.show()

    def change_my_username2(self):
        # 得到数据
        data = sqls.select_user(login_ui.data_mysql, name=login_ui.data_user["username"])
        data_username = data[0][0]
        data_password = data[0][1]
        # 用户名不能旧新一致
        if self.ui.new_username.text() != data_username:
            sqls.delete_user(login_ui.data_mysql,data_username)
            sqls.add_user(login_ui.data_mysql,self.ui.new_username.text(),data_password)
            self.exit()

        else:
            self.ui.label_word.setText("用户名前后一致，不予修改")

    def all_teacher(self):
        # 显示
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(7)

class Sdept:
    def __init__(self):
        #加载
        qfile = QFile("data/ui/sdept.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.slot()
        self.hide()

        header1 = CheckBoxHeader()
        self.ui.student_table.setHorizontalHeader(header1)
        header1.select_all_clicked.connect(header1.change_state)  # 行表头复选框单击信号与槽
        self.ui.student_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.student_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def hide(self):
        self.ui.student.hide()

    def slot(self):
        self.ui.student_button.clicked.connect(self.select_student)
        self.ui.student_button2.clicked.connect(self.select2_student)

    def select_student(self):
        # TODO 检索查询
        self.ui.student.show()
        # 查询现在这个院有什么班级
        # 首先查询是在什么院
        data = sqls.select_sdept(mysql_word=login_ui.data_mysql, id=login_ui.data_user["username"])
        data = data[0][1]
        print(data)
        # 查询这个院有什么班，依次加到box中
        data_class = sqls.select_class(mysql_word=login_ui.data_mysql, sdept_name=data)
        for c in data_class:
            self.ui.select_class_box.addItem(c[0])

        # 我们需要添加信息在student表中
        data = sqls.select_one_student(mysql_word=login_ui.data_mysql, sdept=data)
        print(data)
        self.ui.student_table.setRowCount(len(data))
        for row in range(0, len(data)):
            for column in range(0, len(data[0])):
                checkbox = QCheckBox()
                all_header_checkbox.append(checkbox)
                self.ui.student_table.setCellWidget(row, 0, checkbox)  # 设置表格可选项
                self.ui.student_table.setItem(row, column+1, QTableWidgetItem(f"{data[row][column]}"))

    def select2_student(self):
        print(self.ui.select_sdept_box.currentText())
class CheckBoxHeader(QHeaderView):
    """自定义表头类"""
    # 自定义 复选框全选信号
    select_all_clicked = Signal(bool)
    # 这4个变量控制列头复选框的样式，位置以及大小
    _x_offset = 0
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                    # 当用户点击了行表头复选框，发射 自定义信号 select_all_clicked()
                self.select_all_clicked.emit(self.isOn)

                self.updateSection(0)
        super(CheckBoxHeader, self).mousePressEvent(event)

    # 自定义信号 select_all_clicked 的槽方法
    def change_state(self, isOn):
        # 如果行表头复选框为勾选状态
        if isOn:
            # 将所有的复选框都设为勾选状态
            for i in all_header_checkbox:
                i.setCheckState(Qt.Checked)
        else:
            for i in all_header_checkbox:
                i.setCheckState(Qt.Unchecked)






app = QApplication(sys.argv)

login_ui = Login()
sdept_ui = Sdept()
register_ui = Register()
student_ui = Student()
root_ui = Root()
login_ui.ui.show()
sys.exit(app.exec_())

























