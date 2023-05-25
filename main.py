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


class Main:
    def __init__(self):
        with open("data\mysql.json", "r") as fp:
            self.data = json.load(fp)




















app = QApplication(sys.argv)
import login
login_ui = login.Login()
login_ui.ui.show()
sys.exit(app.exec_())

























