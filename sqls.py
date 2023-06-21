import pymysql
import json


def InitializeDatabase(mysql_word, mydatabase):
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"],user = mysql_word["username"],password =mysql_word["password"],database = "mysql")
    cursor = db.cursor()
    # 开始初始化操作
    sql = f"drop database if exists {mydatabase}"
    cursor.execute(sql)
    sql = f"create database {mydatabase}"
    cursor.execute(sql)
    sql = f"""create table {mydatabase}.user(
    name varchar(20),
    password varchar(20)
    );
    """
    cursor.execute(sql)
    sql = f"""
    create table {mydatabase}.student(
    s_id char(10)  unique,
    s_name char(10) ,
    s_sex char(1) ,
    s_phone char(11),
    s_email varchar(30),
    s_home varchar(20) ,
    s_dorm char(10),
    s_dept varchar(20),
    s_class varchar(20)
    );
    """
    cursor.execute(sql)
    sql=f"""
    create table {mydatabase}.score(
    s_id char(10),
    s_name char(20),
    c_name char(10),
    `score` int(3),
    `rank` varchar(5)
    );
    """
    cursor.execute(sql)
    sql=f"""
    create table {mydatabase}.course(
    class_name varchar(20) ,
    course_name varchar(20),
    teacher_id varchar(20)
    );
    """
    cursor.execute(sql)

    sql=f"""
    create table {mydatabase}.teacher(
    t_id char(5),
    t_name char(10) ,
    t_sex char(1) ,
    s_phone char(11),
    e_emile varchar(30),
    s_home varchar(20) 
    );
    """
    cursor.execute(sql)


    sql=f"""
    create table {mydatabase}.sdept(
    sdept_id varchar(10),
    `sdept_name` varchar(20),
    `sdept_username` varchar(10)
    );
    """
    cursor.execute(sql)

    sql=f"""
    create table {mydatabase}.class(
    class_name varchar(20),
    sdept varchar(20)
    );
    """
    cursor.execute(sql)
    sql=f"""
    create table {mydatabase}.class_student(
    class_name varchar(20),
    student_id varchar(20)
    );
    """
    cursor.execute(sql)
    db.commit()
    sql=f"""INSERT INTO {mydatabase}.user values ('fengyangdong', '123456'),("100001", "123456"),("10001","123456"),("1001","123456");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.sdept values (1001, "计算机院", "小王");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.teacher(t_id,t_name) values (10001, "小红");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.student values (100001, "冯杨栋","男","18009065031",'1584169835@qq.com',"四川绵阳","1社311","计算机院","大数据2101"); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.user values (100001, 123); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.class values ("大数据2101", '计算机院'); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.course values ("大数据2101", '数据库mysql',"10001"); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.class_student values ("大数据2101", 100001); """
    cursor.execute(sql)

    db.commit()
    db.close()


def select_user(mysql_word, name=""):
    where = False
    temp = False
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
    select * from user"""
    if name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  name = '{name}'"
        temp = True
    print(sql)
    cursor.execute(sql)
    name = cursor.fetchall()
    db.close()
    return name


def select_course(mysql_word):
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],
                         database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        select * from course"""
    cursor.execute(sql)
    name = cursor.fetchall()
    db.close()
    return name
def add_user(mysql_word,username,password):
    """
    没什么说的，简单，自己看
    :param mysql_word: 传进来的连接数据库信息
    :param username: 用户名
    :param password: 密码
    :return: 无
    """
    # 不能改成关键字参数
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        insert into user values('{username}', '{password}')"""

    cursor.execute(sql)
    db.commit()
    db.close()


def select_one_student(mysql_word, id="", sdept=""):
    where = False
    temp = False
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    # 如果是dict，说明传进来的是user.json
    sql = f"""select * from student"""
    if id != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  s_id = '{id}'"
        temp = True
    if sdept != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  s_dept = '{sdept}'"
        temp = True
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data


def change_student(mysql_word, user_word="",user="",sex="",phone="",email="",home=""):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""update student set s_id = '{user_word['username']}'"""

    if user != "":
        sql += f""" ,s_name = '{user}' """
    if sex != "":
        sql += f""" ,s_sex = '{sex}' """
    if phone != "":
        sql += f""", s_phone = '{phone}' """
    if email != "":
        sql += f""" ,s_email = '{email}' """
    if home != "":
        sql += f""" ,s_home = '{home}' """
    sql += f"""where s_id = '{user_word['username']}'"""
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()


# def _user(mysql_word, name="",new_name="", new_password=""):
#     where = False
#     temp = False
#     db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
#     cursor = db.cursor()
#     sql = f"""alter user set """
#     if id != "":
#         if where == False:
#             sql += " where "
#             where = True
#         if temp != False:
#             sql += " , "
#         sql +=f"  s_id = '{id}'"
#         temp = True
def select_sdept(mysql_word, id=""):
    where = False
    temp = False
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql=f"""
    select * from sdept """
    if id != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  sdept_id = '{id}'"
        temp = True

    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def add_sdept(mysql_word, id, name, user):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        insert into sdept value ('{id}','{name}','{user}')
        """
    cursor.execute(sql)
    db.commit()
    db.close()

# def add_root(mysql_word, user):
#     db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
#     cursor = db.cursor()
#     sql = f"""
#         insert into user value ('{user}')
#         """
#     cursor.execute(sql)
#     db.commit()
#     db.close()

def delete_sdept(mysql_word, id):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from sdept where sdept_id = {id}
        """
    cursor.execute(sql)
    db.commit()
    db.close()


def delete_user(mysql_word, id):
    # 不能改成关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from user where name = '{id}'"""
    cursor.execute(sql)
    db.commit()
    db.close()

def select_class(mysql_word, sdept_name=""):
    where = False
    temp = False
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""select * from class """
    if sdept_name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  sdept = '{sdept_name}'"
        temp = True
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data