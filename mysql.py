import pymysql
db = pymysql.connect(host="localhost", user="root", password="123456",
                     database="test_1")
cursor = db.cursor()
while True:

    sql = input("请输入")
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    print(data)
db.close()