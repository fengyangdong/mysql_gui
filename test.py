import pymysql

# 打开数据库连接

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='end_hole')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# print("Database version : %s " % data)



while 1:
    sql="select * from data where id >= 15"
    data = cursor.execute(sql)
    print(data)
    data = cursor.fetchone()
    print(data)
    data = cursor.fetchone()
    print(data,type(data))
    print(data[0],data[1])
    eee = input("请输入：")
    if eee == "q":
        break




# 关闭数据库连接
db.close()



import json
with open("data\mysql.json", "r") as fp:
    data = json.load(fp)
print(data)
data['database'] = "end_hole"
with open("data\mysql.json", "w") as fp:
    json.dump(data, fp, ensure_ascii=False)







class AppMain:
    def __init__(self):
        qfile = QFile("ui/app.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        self.slot()

    def slot(self):
        self.ui.button_dism.clicked.connect(self.open_dism)
        self.ui.button_ccleaner.clicked.connect(self.open_ccleaner)
        self.ui.button_spacesniffer.clicked.connect(self.open_spacesniffer)
        self.ui.button_exit.clicked.connect(self.exit_end)
        self.ui.button_geek.clicked.connect(self.open_geek)
    def open_dism(self):
        os.startfile(r'F:\OneDrive\工具\app\清理软件\Dism++\Dism++x86.exe')

app = QApplication(sys.argv)
Main0 = MenuUi()
PassWord_ui = PassWordMain()
Web_ui = WebMain()
App_ui = AppMain()

from main_FuncMain import FuncMain
Func_ui = FuncMain()

Main0.ui.show()
sys.exit(app.exec_())