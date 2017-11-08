#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# 很多内置的函数，比如
p = hex(15)
print(p)
p = abs(-15)
print(p)
p = max(15, 20)
print(p)


# 定义一个函数
def my_abs(x):
    # 检查参数
    if not isinstance(x, (int, float)):
        raise TypeError("your param is not correct")

    if x >= 0:
        return x
    else:
        return -x


# pass语句用于空函数
def null_func():
    pass


# 返回不止一个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # 实际上是返回了个tuple


print(move(5, 5, 20))  # 实际上是返回了个tuple


# 练习一个二次方程求根
def find_function_res(a, b, c):
    dart = b * b - 4 * a * c
    if dart < 0:
        print('no values')
        return
    else:
        return ((-1) * b + math.sqrt(dart)) / (2 * a), ((-1) * b - math.sqrt(dart)) / (2 * a)


print(find_function_res(1, 3, -4))


# 默认参数
def my_power(x, n=2):
    res = 1
    while n > 0:
        res = x * res
        n = n - 1
    return res


print(my_power(5))
print(my_power(5, 3))


# 默认参数的规则：默认的写在后面,默认参数指向不变对象
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 如果不按照顺序传递参数，就把参数名字写上
enroll('yxnne', 'male', city='xi\'an')


# 可变数量的参数,加个*，传进来的就当做tuple对象
def calc(*numbers):
    sumarys = 0
    for n in numbers:
        sumarys = sumarys + n * n
    return sumarys


print(calc(1, 2, 3, 4))

# 如果已经有一个tuple 了，传递到函数中怎么传？
# 繁琐的方法：
tuple_exist = (1, 2, 3, 4)
print(calc(tuple_exist[0], tuple_exist[1], tuple_exist[2], tuple_exist[3]))
# 简单的方法：tuple加 * 就转换成可变参数
print(calc(*tuple_exist))


# 关键字参数：** **后面的会作为dictionary使用
def person(name, age, **aa):
    print('name:', name, 'age:', age, 'other param is:', aa)


person('yxnne', 29, city="xian", goal="very big goals")
# 也可以先封装dict然后用**转换成关键字参数
extra_dict = {'city': "xian", 'task': "earn money"}
person('yxn', 30, **extra_dict)


# 关键字检查
def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person2('a', 8, city="CDC")


# 命名关键字参数 keyword-only,使用的时候必须有名字,
# * 后面测参数默认为这种
def test(test_p, *, a, b):
    print('test is ', test_p)
    print('a is :', a)
    print('b is :', b)

# def person(name, age, *args, city, job):假设这样子定义了，args是可变参数
# 那么 city 和 job 也是默认关键字参数了


# test('a')
test('a', a=20, b=True)



