import matplotlib.pyplot as plt

# lbj point
lbj_p = [20.9, 27.2, 31.4, 27.3, 30.0, 28.4, 29.7, 26.7, 27.1, 26.8, 25.3, 25.3, 26.4, 27.2, 28.4]
# year
x_year = ['03', '04', '05', '06', '07', '08', '09', '10','11', '12', '13', '14', '15', '16', '17']

# 2.增加点可读性
plt.title("Who\'s LBJ", fontsize=24)  # 标题
plt.xlabel("Year", fontsize=18)  # X轴设置
plt.ylabel("Points", fontsize=18)  # Y轴设置
plt.tick_params(axis='both', labelsize=14)

# 1.三句话的代码
plt.plot(x_year, lbj_p, linewidth=2, color='red', marker='o', linestyle='solid')
plt.show()