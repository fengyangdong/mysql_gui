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
    `score` int(3)
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
    s_home varchar(20) ,
    s_sdept varchar(20)
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
    sql=f"""INSERT INTO {mydatabase}.user values ('fengyangdong', '123456'),
    ("100001", "123456"),("100002", "123456"),
    ("100003", "123456"),("100004", "123456"),("100005", "123456"),("100006", "123456"),("100007", "123456"),
    ("100008", "123456"),("100009", "123456"),("100010", "123456"),("100011", "123456"),("100012", "123456"),
    ("100013", "123456"),("100014", "123456"),("100015", "123456"),("100016", "123456"),("100017", "123456"),
    ("100018", "123456"),("100019", "123456"),("100020", "123456"),("100021", "123456"),("100022", "123456"),
    ("100023", "123456"),("100024", "123456"),("100025", "123456"),("100026", "123456"),("100027", "123456"),
    ("100028", "123456"),("100029", "123456"),("100030", "123456"),("100031", "123456"),("100032", "123456"),
    ("100033", "123456"),("100034", "123456"),("100035", "123456"),("100036", "123456"),("100037", "123456"),
    ("100038", "123456"),("100039", "123456"),("100040", "123456"),("100041", "123456"),("100042", "123456"),
    ("100043", "123456"),("100044", "123456"),("100045", "123456"),("100046", "123456"),("100047", "123456"),
    ("100048", "123456"),("100049", "123456"),("100050", "123456"),("100051", "123456"),("100052", "123456"),
    ("100053", "123456"),("100054", "123456"),("100055", "123456"),("100056", "123456"),("100057", "123456"),
    ("100058", "123456"),("100059", "123456"),("100060", "123456"),("1001","123456"),("1001", "123456"),
    ("1002", "123456"),("1003", "123456"),("1004", "123456"),("10001", "123456"),("10002", "123456"),
    ("10003", "123456"),("10004", "123456"),("10005", "123456"),("10006", "123456"),
    ("10007", "123456"),("10008", "123456");"""
    cursor.execute(sql)
    sql=f"""INSERT INTO {mydatabase}.sdept VALUES (1001, "计算机院", "小王"),
                                    (1002, "理学院", "小红"),
                                    (1003, "土木院", "小黑"),
                                    (1004, "外语院", "小玉");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.teacher(t_id,t_name,s_sdept) values (10001, "小红", "理学院"),
                                                                (10002, "张老师","理学院"),
                                                                (10003, "张老师","计算机院"),
                                                                (10004, "张老师","计算机院"),
                                                                (10005, "张老师","计算机院"),
                                                                (10006, "张老师","土木院"),
                                                                (10007, "张老师","土木院"),
                                                                (10008, "张老师","外语院");"""
    cursor.execute(sql)
    sql=f"""insert into {mydatabase}.student values (100001, "冯杨栋","男","18009065031",'1584169835@qq.com',"四川绵阳","1社311","计算机院","大数据2101"),
                                                    (100002, "张三", "男", "18009065032", 'zhangsan@example.com', "北京", "2社101", "计算机院", "大数据2101"),
                                                    (100003, "李四", "女", "18009065033", 'lisi@example.com', "上海", "3社201", "计算机院", "大数据2101"),
                                                    (100004, "王五", "男", "18009065034", 'wangwu@example.com', "广州", "4社401", "计算机院", "大数据2101"),
                                                    (100005, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100006, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100007, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100008, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100009, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100010, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100011, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100012, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100013, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100014, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100015, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "大数据2101"),
                                                    (100016, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100017, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100018, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100019, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100020, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100021, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100022, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100023, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100024, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100025, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100026, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100027, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100028, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100029, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100030, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "计算机院", "信息技术2101"),
                                                    (100031, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100032, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100033, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100034, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100035, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100036, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100037, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100038, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100039, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100040, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100041, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100042, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100043, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100044, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100045, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "土木院", "建筑学2101"),
                                                    (100046, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100047, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100048, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100049, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100050, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100051, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100052, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100053, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100054, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100055, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100056, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100057, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100058, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100059, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"),
                                                    (100060, "赵六", "女", "18009065035", 'zhaoliu@example.com', "深圳", "5社511", "外语院", "日语学2101"); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.class values ("大数据2101", '计算机院'),
    ("信息技术2101", '计算机院'),
    ("数学2101", '理学院'),
    ("物理2101", '理学院'),
    ("建筑学2101", '土木院'),
    ("建筑学2102", '土木院'),
    ("日语学2101", '外语院'),
    ("英语学2101", '外语院'); """
    cursor.execute(sql)
    sql = f"""insert into {mydatabase}.course values ("大数据2101", '数据库mysql',"10001"),
    ("大数据2101","linux课程","10001"),("信息技术2101","linux课程","10001"),
    ("信息技术2101","数据库mysql","10001"),("英语学","英语课程","10008"),
    ("建筑学2101","建筑专业","10007"),("日语学2101","日语专业","10008"); """
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
    name1 = cursor.fetchall()
    db.close()
    return name1


def select_course(mysql_word, id="",name=""):
    where = False
    temp = False
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],
                         database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        select * from course"""
    if id != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " and "
        sql +=f"  teacher_id = '{id}'"
        temp = True
    if name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " and "
        sql +=f"  course_name = '{name}'"
        temp = True
    print(sql)
    cursor.execute(sql)
    name = cursor.fetchall()
    db.close()
    return name

def select_score(mysql_word, id="",name=""):
    where = False
    temp = False
    # 连接mysql
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],
                         database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        select * from score"""
    if id != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " and "
        sql +=f"  s_id = '{id}'"
        temp = True
    if name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " and "
        sql +=f"  c_name = '{name}'"
        temp = True
    print(sql)
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

def add_teacher(mysql_word,id="",name="",sex="",phone="",email="",home="",sdept=""):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql=f"""insert into teacher values ('{id}','{name}','{sex}','{phone}','{email}','{home}','{sdept}')"""
    cursor.execute(sql)
    db.commit()
    db.close()


def add_course(mysql_word,class_name,course_name,teacher_id):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql=f"""insert into course values ('{class_name}','{course_name}','{teacher_id}')"""
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()
def select_one_student(mysql_word, id="", sdept="",class_name="",name=""):
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
    if name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  s_name = '{name}'"
        temp = True
    if sdept != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  s_dept = '{sdept}'"
        temp = True

    if class_name != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  s_class = '{class_name}'"
        temp = True
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data


def select_teacher(mysql_word, id=""):
    where = False
    temp = False
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    # 如果是dict，说明传进来的是user.json
    sql = f"""select * from teacher"""
    if id != "":
        if where == False:
            sql += " where "
            where = True
        if temp != False:
            sql += " , "
        sql +=f"  t_id = '{id}'"
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
    # 不能使用关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        insert into sdept value ('{id}','{name}','{user}')
        """
    cursor.execute(sql)
    db.commit()
    db.close()

def add_score(mysql_word, id, s_name, c_user,score):
    # 不能使用关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        insert into score value ('{id}','{s_name}','{c_user}','{score}')"""
    cursor.execute(sql)
    db.commit()
    db.close()

def delete_score(mysql_word, id):
    # 不能使用关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from score where s_id = '{id}'"""
    cursor.execute(sql)
    db.commit()
    db.close()
def add_student(mysql_word,id="",name="",sex="",phone="",email="",home="",dorm="",sdept="",s_class=""):
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql=f"""insert into student values ('{id}','{name}','{sex}','{phone}','{email}','{home}','{dorm}','{sdept}','{s_class}')"""
    cursor.execute(sql)
    db.commit()
    db.close()
def add_class(mysql_word, sdept, class_name):
    # 不能使用关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],
                         database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
            insert into class value ('{class_name}','{sdept}')"""
    print(sql)
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


def delete_student(mysql_word, id):
    # 不能改成关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from student where s_id = '{id}'"""
    cursor.execute(sql)
    db.commit()
    db.close()


def delete_teacher(mysql_word, id):
    # 不能改成关键字参数
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from teacher where t_id = '{id}'"""
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()


def delete_course(mysql_word, class_name,name,teacher):
    # 不能改成关键字参数
    # 因为这个字段比较少，而且不可能出现空的情况，所以直接全部删除了
    db = pymysql.connect(host=mysql_word["hostname"], user=mysql_word["username"], password=mysql_word["password"],database=mysql_word["database"])
    cursor = db.cursor()
    sql = f"""
        delete from course where class_name = '{class_name}' and course_name='{name}' and teacher_id = '{teacher}' """
    print(sql)
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