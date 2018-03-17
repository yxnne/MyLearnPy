import matplotlib.pyplot as plt

# lbj point
lbj_p = [20.9, 27.2, 31.4, 27.3, 30.0, 28.4, 29.7, 26.7, 27.1, 26.8, 25.3, 25.3, 26.4, 27.2, 28.4]
# year
x_year = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17']

# 2.增加点可读性
plt.title("Who\'s LBJ", fontsize=24)  # 标题
plt.xlabel("Year", fontsize=18)  # X轴设置
plt.ylabel("Points/Rebound/Assist", fontsize=18)  # Y轴设置
plt.tick_params(axis='both', labelsize=14)

# 加上助攻和篮板？
lbj_r = [5.5, 7.4, 7.1, 6.8, 7.9, 7.6, 7.3, 7.5, 7.9, 8.0, 7.0, 6.0, 7.4, 8.6, 8.2]
lbj_a = [5.9, 7.2, 6.6, 6.0, 7.2, 7.2, 8.6, 7.0, 6.2, 7.3, 6.3, 7.4, 6.8, 8.7, 9.2]
# 1.三句话的代码
plt.plot(x_year, lbj_p, linewidth=2, color='red', marker='o', linestyle='solid', label="points")
plt.plot(x_year, lbj_r, linewidth=2, color='green', marker='o', linestyle='solid', label="rebounds")
plt.plot(x_year, lbj_a, linewidth=2, color='blue', marker='x', linestyle='--', label="assists")

plt.legend()
plt.show()
