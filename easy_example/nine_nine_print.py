# 九九乘法表

# 左上三角格式输出九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print("%d*%d=%2d" % (i, j, i*j), end=" ")
    print("")


def pear(a, b):
    return a + b


print(pear("213", "111"))

print("input 2 nubers and i will add them")

a = input("input a :")
b = input("input b :")

sum = int(a)+int(b)
print("sum of a,b is :", sum)
