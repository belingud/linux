import pymysql

# 1 连接数据库
# host 服务器名
# user 用户名
# password 密码
# db  数据库名
# port 端口，默认是3306 ，可以不写
# charset 连接的字符集
conn = pymysql.Connect(host='10.0.127.148',user='root',password='pddpdd',db='school',port=3306,charset='utf8')
# print(conn.)

# 2创建游标，执行sql，取回服务器返回数据
cursor = conn.cursor()
# print(cursor)

# 3 写sql
sql = "select id,name,sex from test"

# 对于查询来说，result是记录个数
result = cursor.execute(sql)
# print(result)

# 4 获取结果集
# 获取一条记录
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# 取多条
# 如果给定数目不超过总记录数，返回指定的记录，否则返回所有记录
# ((1, 'stephen', 'man'), (2, 'pandd', 'man'))
# print(cursor.fetchmany(2))
# 返回所有记录
# print(cursor.fetchall())
# data = cursor.fetchall()
# # for rec in data:
# #     print(rec,rec[1])
# 5 关闭游标和连接
cursor.close()
conn.close()