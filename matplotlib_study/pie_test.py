import matplotlib.pyplot as plt

labels = 'LoL', 'chicken', 'glory', 'other'
sizes = [15, 30, 65, 10]
explode = (0, 0, 0.1, 0)   # 0.1表示将Hogs那一块凸显出来
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# startangle表示饼图的起始角度
# autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数

plt.show()
