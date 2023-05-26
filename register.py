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


class Register:
    def __init__(self):
        #
        qfile = QFile("data/ui/register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
