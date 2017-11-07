#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件
ageStr = input('input your age : ')
age = int(ageStr)
name = 'yxnne'
if age > 100:
    print("It may not real~~~")
elif 100 >= age > 50:
    print("old man are you")
elif 50 >= age > 30:
    print("real man")
elif 30 >= age > 20:
    print("do you have your wife ?")
else:
    if name == 'yxnne':  # 字符串比较
        print("no questions!")

# 循环
# for in
one_ten_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumary = 0
for i in one_ten_list:
    sumary = sumary + i
print("sum is ", sumary)

# range(x) 函数 计算1--100的和，生成[0,x)整数集合
sumary = 0
for i in range(101):
    sumary = sumary + i
print("sum is ", sumary)

# while 技术100内基数和偶数和
sumary = 0
n = 99
while n > 0:
    sumary = sumary + n
    n = n - 2
print(sumary)

sumary = 0
n = 100
while n > 0:
    sumary = sumary + n
    n = n - 2
print(sumary)
