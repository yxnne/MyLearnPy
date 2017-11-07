#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python源文件起始行的两行注释
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出
# 可能会有乱码。

# 注释应该这么写 注意有个空格
# 输出print
print("Hi,yxnne in python")
# 多行文字'''    ''' 包裹起来，或者使用转移符\n
print('''many lines as 
you see''')
print('many lines as \nyou see')
s3 = r'Hello, "Bart"'       # r 省略转义字符
s4 = r'''Hello,             
Lisa!'''                    # r 省略换行符
print(s3)
print(s4)

# input()函数，接收用户字符输入，enter确认
print("---------can u input your name ?")
name = input()
print("input is ", name)

# 基本类型
# 整形/浮点/字符串/布尔(True and False)
# 空 None

# 变量：Python是动态语言，所谓动态语言就是弱类型语言，不用声明定死类型
a = 123
print(a)
a = "shit , changed"
print(a)

# len()函数
# 1）字符串长度；2）字节数
count = len(b'\xe4\xb8\xad\xe6\x96\x87')  # 字节前面有个小写b作为前缀
strZhw = b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8")
print('中文一个字3个字节', strZhw, count)
count = len('中文')
print(count)

# 格式化，类似C语言 ，%s 字符串 %d 整数 %f 浮点数 保留两位%.2f
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print("十除以三保留两位小数是：%.2f" % ((5 + 5)/3))
