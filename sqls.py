import pymysql


def InitializeDatabase(mydatabase):
    db = pymysql.connect(host='localhost',user = 'root',password = '123456',database = "mysql")
    cursor = db.cursor()
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