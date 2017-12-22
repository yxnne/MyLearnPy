import numpy as np
import matplotlib.pyplot as plt


labels = ['语文', '英语', '科学', '文艺', '体育', '游戏']
# 数据个数
dataLength = 6
# 数据
data = [8, 6, 9, 1, 2, 3]
# 计算角度，返回等差数列
angles = np.linspace(0, 2*np.pi, dataLength, endpoint=False)
# 要拼接
data = np.concatenate((data, [data[0]]))  # 闭合
angles = np.concatenate((angles, [angles[0]]))  # 闭合


# 加一个data
# data2 = [6, 4, 2, 1, 6, 9]
# data2 = np.concatenate((data2, [data2[0]]))


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)  # polar参数！！
ax.plot(angles, data, 'bo-', linewidth=2)  # 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)  # 填充

# ax.plot(angles, data2, 'go-', linewidth=2)  # 画线
# ax.fill(angles, data2, facecolor='b', alpha=0.25)  # 填充

ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei") # 方法用于设置极坐标角度网格线显示
# ax.set_title("matplotlib雷达图", va='bottom', fontproperties="SimHei")
ax.set_rlim(0,10)
ax.grid(True)
plt.show()
