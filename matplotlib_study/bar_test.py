import numpy as np
import matplotlib.pyplot as plt
size = 5
a = [2, 5, 4, 3, 2]
b = np.random.random(size)
x = np.arange(size)         # 和range()函数差不多 reange(5) ->[0,1,2,3,4]

total_width, n = 0.8, 4     # 有多少个类型，只需更改n即可
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.legend()
plt.show()
