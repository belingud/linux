import pymysql

conn = pymysql.Connect(host='localhost',user='root',password='123',db='homwork',port=3306,charset='utf8')
cursor = conn.cursor()

sql = "insert into course(cid,name,tid) values(4,'计算机原理',1)"
try:
    # pymysql关闭了自动提交，自动开启了事务
    # 返回值是1表示操作成功，否则失败
    result = cursor.execute(sql)
    print(result)
    conn.commit()  # 必须手动提交
    # 获取新增记录的自增主键的值
    print(cursor.lastrowid)
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()