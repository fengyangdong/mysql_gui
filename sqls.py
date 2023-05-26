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
    name varchar(20) not null ,
    password varchar(20) not null ,
    type int not null
    );
    """
    cursor.execute(sql)
    sql = f"""
    create table {mydatabase}.student(
    s_id char(10) not null unique,
    s_name char(10) not null ,
    s_sex char(1) not null ,
    s_home varchar(20) not null 
    );
    """
    cursor.execute(sql)
    sql=f"""
    create table {mydatabase}.score(
    s_id char(10),
    c_id char(10),
    `score` int(3),
    `rank` varchar(5)
    )
    """
    cursor.execute(sql)
    sql=f"""
    create table {mydatabase}.cource(
    c_id char(10) not null ,
    c_name varchar(20),
    c_teacher varchar(20)
    );
    """
    cursor.execute(sql)
    db.close()


def in_determine(mysql_word, username, passwrod):
    print(1)
    # 连接mysql

    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
    select * from user where name = {username}
    """
    cursor.execute(sql)
    name = cursor.fetchall()
    if name == "":
        print("没有")
    return 1