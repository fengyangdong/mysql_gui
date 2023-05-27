import pymysql



word = "12"


db = pymysql.connect(host='localhost', user='root', password='123456',database='test_1')
cursor = db.cursor()
sql = f"""
select * from user
"""
sql += "where name = "
sql += word
cursor.execute(sql)
data = cursor.fetchall()
print(data)