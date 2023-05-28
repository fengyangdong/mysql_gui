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
    e_emile varchar(30),
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
    create table {mydatabase}.cource(
    class_name varchar(20) ,
    course_name varchar(20),
    teacher_name varchar(20)
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
    db.commit()
    sql=f"""INSERT INTO {mydatabase}.user values ('fengyangdong', '123456');"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.sdept values (1001, "计算机院", "小王");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.teacher(t_id,t_name) values (10001, "小红");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.student(s_id,s_name) values (100001, "冯杨栋"); """
    cursor.execute(sql)

    db.commit()
    db.close()


def select_user(mysql_word):
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
    select * from user
    """
    cursor.execute(sql)
    name = cursor.fetchall()
    print(name,type(name))
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
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = """
        insert into user values(%s, %s)
        """ % (username, password)

    cursor.execute(sql)
    db.commit()
    db.close()


def select_student(mysql_word, student):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        select * from student where s_id = {student}
    """
    data = cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


def select_sdept(mysql_word):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql=f"""
    select * from sdept
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def add_sdept(mysql_word, id, name, user):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        insert into sdept value ({id},{name},{user})
        """
    cursor.execute(sql)
    db.commit()
    db.close()

def delete_sdept(mysql_word, id):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from sdept where sdept_id = {id}
        """
    cursor.execute(sql)
    db.commit()
    db.close()