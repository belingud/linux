
import hashlib
import pymysql

# 1 连接数据库
# host 服务器名
# user 用户名
# password 密码
# db  数据库名
# port 端口，默认是3306 ，可以不写
# charset 连接的字符集
conn = pymysql.Connect(host='localhost',user='root',password='123',db='homwork',port=3306,charset='utf8')
print(conn)


# 2创建游标，执行sql，取回服务器返回数据
cursor = conn.cursor()
print(cursor)
#
# # 3 写sql
name = input("请输入姓名:")
password = input("请输入密码：")

print(name)
# print(conn.escape_string(name))
# name = conn.escape_string(name)

password = hashlib.sha1(password.encode('utf8')).hexdigest()
print(password)

# 字符串两边必须有单引号
# 这种简单的sql写法，无法预防sql注入攻击,黑客可以通过构造特殊的输入，绕过用户名和密码判断
"""
请输入姓名:sdfsdf' or 1 or '1
请输入密码：sdfs
"""
# sql = "select uid,name from user where name='%s' and password='%s'"%(name,password)
# print(sql)
#
# 防止sql注入有以下两种写法：
# escape_string转义输入的特殊字符

# 2 通过excute（query,args)
sql = "select uid,name from user where name=%s and password=%s"
result = cursor.execute(sql,(name,password))
print(cursor._executed)

# # 对于查询来说，result是记录个数
# result = cursor.execute(sql)
if result>0:
    print("登录成功")
else:
    print("登录失败，用户名或密码错误")


# # 5 关闭游标和连接
cursor.close()
conn.close()