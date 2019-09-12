import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data = np.load('./populations.npz')

print(data.files)

new_data_temp = np.delete(data['data'], -1, 0)
new_data = np.delete(new_data_temp, -1, 0)

print(new_data)
print(data['feature_names'])

# name = data['feature_names']  # 提取其中的columns数组，视为数据的标签
values = new_data  # 提取其中的values数组，数据的存在位置

pl = plt.figure(figsize=(8, 6))  # 设置画布

# 创建第一个子图
pl.add_subplot(2, 1, 1)

# 绘制散点1
plt.scatter(range(1, 21, 1), values[-1::-1, 1], marker='o', c='red')
# 绘制散点2
plt.scatter(range(1, 21, 1), values[-1::-1, 2], marker='D', c='blue')
# 绘制散点3
plt.scatter(range(1, 21, 1), values[-1::-1, 3], marker='v', c='yellow')
# 绘制散点4
plt.scatter(range(1, 21, 1), values[-1::-1, 4], marker='s', c='green')
# 绘制散点5
plt.scatter(range(1, 21, 1), values[-1::-1, 5], marker='*', c='pink')
plt.xlabel('年份')  # 添加横轴标签
plt.ylabel('人口数量（万人）')  # 添加纵轴标签
plt.xticks(range(1, 22, 1), values[-1::-1, 0], rotation=45)
plt.title('1996-2015人口数据各特征变化图')  # 添加图表标题
plt.legend(['年末总人口', '男性人口', '女性人口', '城镇人口', '乡村人口'])  # 添加图例
# plt.savefig('../tmp/2000-2017年各产业季度生产总值散点图.png')

# 创建第二个子图
pl.add_subplot(2, 1, 2)

# 绘制散点1
# plt.scatter(range(1, 21, 1), values[-1::-1, 1], marker='o', c='red')
plt.plot(range(1, 21, 1), values[-1::-1, 1], color='r', linestyle='-.')
# 绘制散点2
plt.plot(range(1, 21, 1), values[-1::-1, 2], color='b', linestyle='-.')
# 绘制散点3
plt.plot(range(1, 21, 1), values[-1::-1, 3], color='g', linestyle='-.')
# 绘制散点4
plt.plot(range(1, 21, 1), values[-1::-1, 4], color='m', linestyle='-.')
# 绘制散点5
plt.plot(range(1, 21, 1), values[-1::-1, 5], color='c', linestyle='-.')
plt.xlabel('年份')  # 添加横轴标签
plt.ylabel('人口数量（万人）')  # 添加纵轴标签
plt.xticks(range(1, 22, 1), values[-1::-1, 0], rotation=45)
plt.title('1996-2015人口数据各特征变化图')  # 添加图表标题
plt.legend(['年末总人口', '男性人口', '女性人口', '城镇人口', '乡村人口'])  # 添加图例
# plt.savefig('../tmp/2000-2017年各产业季度生产总值散点图.png')




plt.show()


