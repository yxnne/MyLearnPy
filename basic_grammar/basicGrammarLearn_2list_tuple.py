#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# data structure： list

# List
# 用[]
ls1 = ['shit', 33, 'omg']
print(ls1[1])
print(ls1[2])
# 索引值是负数从最后一个开始数
# 倒数第一个
print(ls1[-1])

# append()函数：追加
ls1.append("shit")
# 遍历下
print("------开始遍历------")
for i in ls1:
    print(i)
print("------结束遍历------")

# insert()指定位置插入
ls1.insert(0, "oh")

# 入栈出栈操作 append and pop,没有push
last = ls1.pop()
print("last thing is : ", last)

# 插入布尔
ls1.append(True)

# 多维数组
ls2 = [1, 2, 3, ["a", "b"]]


# tuple 不可变列表，用()
# 定义以后值不可变,访问元素方法和list相同，没有append，没有insert等
# 能用tuple不用list
tup = (1, 2, 3, "do la mi")
print(tup[3])
# 定义空tuple
tup_null = ()
# 定义一个元素的tuple
tup_one = (1, )
# 注意 不可变是引用
tup_test = (1, 2, 3, ["aaa", "bbb"])
print(r'before "change"', tup_test)
tup_test[3][0] = "oh"
tup_test[3][1] = "shit"
print(r'after "change"', tup_test)


# def func_viewlist(ls):
#     for item in ls:
#         print(item)




