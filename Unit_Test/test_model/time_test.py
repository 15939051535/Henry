#coding=utf-8
# def each_list(list_name):
#     for yuansu in list_name:
#         if isinstance(yuansu, list):
#             each_list(yuansu)
#         else:
#             print (yuansu)
#
#each_list(new_list)

list = [{"username": "111111", "password": "222222"},
        {"username": "333333", "password": "444444"}]

def ttime():
    import time
    import random
    num = random.uniform(0.1, 5)
    time.sleep(num)

def sk(s):
    print s,

for i in list:
    print (i["username"])
    print (i["password"])
    str1 = i["username"]
    str2 = i["password"]
    for m in (str1):
        ttime()
        sk(m)
    for n in (str2):
        ttime()
        sk(m)


username = '999555'
for i in str(username):
    ttime()
    username.send_keys(str(i))


Name = ['Stella', 'Kay']
ID = [1, 3]
result = [(a, b) for a in ID for b in Name]

#循环读取列表数值
#http://blog.csdn.net/u010003835/article/details/50770296
#http://blog.csdn.net/lclcy306/article/details/38733215
