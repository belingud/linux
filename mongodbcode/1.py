from pymongo import MongoClient
import re

# 1.连接mongo
mg = MongoClient(host='127.0.0.1',port=27017)
# print(mg)

# 2 连接数据库
db = mg.student

# print(db)

# 查询
# 返回是可迭代对象
# data = db.student.find()
# data = db.student.find({'sname':{'$regex':'马'}})
# data = db.student.find({'sname':re.compile("马")})
# data = db.student.find()
# for rec in data:
#     print(rec)

# insert
# db.course.insert({'name':'计算机原理'})

# update
# db.course.update({'cno':'101'},{'$set':{'cname':'数据分析'}})

# remove
db.course.remove({'cno':'101'})

data = db.course.find()
print(list(data))

# 关闭连接
mg.close()

