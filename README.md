# mysql_gui








# 实现过程
## 表结构
### user
用户表，主要功能就是存储登录的用户名和密码，以及等级和学号，超级管理员是1，老师是2，学生是3
超级管理员和老师只能通过超级管理员进行创建，学生的user可以自己创建，也只有学生是有学号的，其他的都是0，
学生创建user必须先得有学号才行
### student
学生信息表，里面就是有很多信息，添加学生信息表，只能是先通过老师或者超级管理员进行添加，老师创建只能创建自己班的学生

