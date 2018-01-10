# 从入门到实践的第3单元代码
# List

# 最后一个元素索引是-1

# 添加列表元素，append()添加到末尾
listTest = []
print(listTest)

listTest.append(123)  # 在末尾添加
print(listTest)

listTest.insert(0, 456)  # 在0索引位置添加
print(listTest)

del listTest[-1]  # 删除末尾
print(listTest)

poped = listTest.pop()  # 弹出最后一个
print(poped)
print(listTest)

listTest = [1, 2, 3, 4]
print(listTest.pop(1))  # 弹出任意位置元素

listTest.remove(4)
print(listTest)  # 根据值删除元素

# 组织列表
# 排序原列表
listTest = ['a', 'c', 'b', 'e', 'd']
listTest.sort()  # 列表排序
print(listTest)
# 反向
listTest.sort(reverse=True)
print(listTest)

# 返回排序列表
listTest = [3, 2, 9, 8, 1]
lisSorted = sorted(listTest)
print("listTest is :" + str(listTest))
print("sorted one is :" + str(lisSorted))

# 翻转列表
listTest = ["b", "o", "r"]
listTest.reverse()
print(listTest)
