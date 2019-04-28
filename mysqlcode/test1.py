# sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}"
#
# paras = {'fields':'*',
#          'table':'user',
#          'where':'',
#          'groupby':'',
#          'having':'',
#          'orderby':'',
#          'limit':''
#          }
# sql = sql.format(**paras)
#
# print(sql)
# 任意位置参数
# sql1 = "a={},b={}".format(1,20)
# 任意关键字参数
# sql1 = "a={c},b={b},c={a}".format(b=20,a=1,c=23)
# sql1 = "a={c},b={b},c={a}".format(**{'a':1,'b':20,'c':23})
# print(sql1)

# 元组解包
# a, b = 1, 2
# a, *_,b = 1,2,3,4,5

# a , b = [1,3]

# print(a,b,_)
# print(a,b)
# for a,b in [(1,2),(3,4)]:
#     print(a,b)

d = {'sid':10,'name':'tom'}
# sql = "insert into student (sid,name) values(10,'tom')"

values = ''
for key in d:
    if isinstance(d[key],str):
        values += "'" + str(d[key])+"',"
    else:
        values += str(d[key]) + ","
print(values)