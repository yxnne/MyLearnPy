#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 引用其他文件的函数
from basic_grammar.basicGrammarLearn_5function import my_abs

# dict字典，就是map
dictionay = {}      # 申明空字典
dictionay['yxnne'] = "cool man"
dictionay['ax'] = "nice"
print('yxnne is :', dictionay['yxnne'])
print('ax is :', dictionay['ax'])
# print(dictionay['jerk'])
a = dictionay.get('jerk', -1)
print("jerk的值是(如果jerk不存在就返回-1) :", a)

# set
# 创建set，要在构造方法中传入一个list，list中相同的元素呗过滤了
set1 = set([1, 2, 3, 4, 5, 6, 6])
set1.add("boom")
set1.add(1)
print(set1)
# 集合操作
set2 = set([0, 1, 2, 3])
print('交集', set1 & set2)
print('并集', set1 | set2)



print(my_abs(-24))

dic ={"name":'yxmm'}

for k in dic:
    print("dic k-v is " + dic[k])

for k in dic.keys():
    print("k is "+ k)

for v in dic.values():
    print("v is " + v)

# declear dictionary

d = {} # empty dictionary

d['name'] = 'yxnne'

d['age'] = 20

d['del'] = 'fake'

print('d ->' + str(d))

del d['del']

print('d ->' + str(d))