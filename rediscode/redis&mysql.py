import redis

from DBHelper import DBHelper

"""
1.查找数据，首先到redis查找
   2.如果找到，则直接使用
   3. 如果找不到，去mysql中查找
       4 在mysql找到了，首先将数据添加redis中，然后再使用
       5 如果没找到，报错

"""
red = redis.StrictRedis()
db = DBHelper('student')

# 1 在redis中查找
sno = input("请输入学号：")
# 键就是学号
student = red.hgetall(sno)

if student:
    # 2 打印
    print("redis:")
    print(student)
else:
    #     3 到mysql中查找
    data = db.where(sid=sno).select()
    print("mysql:",data)
    # 4 将数据添加到reids
    if data:

        red.hmset(sno,data[0])
    else:
        print("mysql没有信息")
