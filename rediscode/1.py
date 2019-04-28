import redis


# 连接redis服务器
"""
 host='localhost',   服务器地址
 port=6379,    端口
 db=0,    数据库，默认是0号库
 password=None,   密码  requirepass 
"""
# red = redis.Redis()
red = redis.StrictRedis()
# print(red)

# String
red.set('name','李文涛')
# 返回i的是二进制字符串
data = red.get('name')

# 删除key
red.delete('name')
print(data, data.decode('utf8'))


#
