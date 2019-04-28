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
# 字符串两边必须有单引号
sql = "select sid,name from student where name='%s'"%name
print(sql)
#
# # 对于查询来说，result是记录个数
result = cursor.execute(sql)
# # print(result)
#
# # 4 获取结果集
print(cursor.fetchall())
# 查看sql语句
print(cursor._executed)
# # 5 关闭游标和连接
cursor.close()
conn.close()