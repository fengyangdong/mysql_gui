import pymysql
import json
import sys
import time
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
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
from main import Login
class Root:
    def __init__(self):
        #加载
        qfile = QFile("data/ui/root.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.slot()

        # 初始化
        self.ui.root_title.setText(f"你是超级管理员，你的编号为{Login.data_user['username']}")
        self.ui.select_sdept.hide()
        self.ui.add_sdept.hide()
    def slot(self):
        self.ui.select_add_sdept.clicked.connect(self.select_add_sdept)
    def select_add_sdept(self):
        self.ui.select_sdept.show()
        sdept_tuple = sqls.select_sdept(Login.data_mysql)
        self.ui.sdept_table.setRowCount(len(sdept_tuple))
        print(len(sdept_tuple))
        print(len(sdept_tuple[0]))
        for row in range(0,len(sdept_tuple)):
            print("row:",row)
            for column in range(0,len(sdept_tuple[0])):
                print("column",column)
                #TODO culi
                self.ui.sdept_table.setItem(row, column, QTableWidgetItem(f"{row},{column}"))
app = QApplication(sys.argv)


root_ui = Root()

sys.exit(app.exec_())