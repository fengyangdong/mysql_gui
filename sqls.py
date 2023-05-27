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
    password varchar(20) ,
    id int not null
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
    s_dept varchar(20)
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
    `sdept_name` varchar(20),
    `sdept_username` varchar(10)
    );
    """
    cursor.execute(sql)

    sql=f"""
    create table {mydatabase}.class(
    class_name varchar(20),
    s_id varchar(10),
    sdept varchar(20)
    );
    """
    cursor.execute(sql)
    db.commit()
    db.close()


    db_1 = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database="mysql")
    cursor = db_1.cursor()
    sql=f"INSERT INTO {mydatabase}.user values ('fengyangdong', '123456', 101)"
    cursor.execute(sql)
    db_1.commit()
    db_1.close()
def in_determine(mysql_word):
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


def add_user(mysql_word,username,password,type,sid):
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    if type == 3:
        sql = """
            insert into user values(%s, %s, %d, %s)
            """ % (username, password, type, sid)
    else:
        sql = """
            insert into user values(%s, %s, %d, 0)
            """ % (username, password, type)
    cursor.execute(sql)
    db.commit()
    db.close()


def select_student(mysql_word, student):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()

    sql = f"""
        select * from student
    """
    data = cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()


    db.close()
    return data