import matplotlib.pyplot as plt
import numpy as np
"""
可视化的工具库
1、构建数据
2、开始画图
3、显示、保存图
"""
# 一、折线图
# 1、构建数据
x = np.arange(1, 8)  # [1,2,3..7]
y = np.array([15, 20, 22, 23, 20, 18, 16])
# y1 = y-5
#
# # 设置中文 和负号可以正常显示
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False
#
# # 2、开始画图
# plt.figure()
# plt.plot(x, y)
# plt.plot(x, y1, marker='o', linestyle='--')
#
# # 2.1 添加描述信息
# plt.title("一周天气信息")
# plt.xlabel("星期信息")
# plt.ylabel("温度")
#
# week_info =['星期1', '星期2', '星期2', '星期3', '星期4', '星期5', '星期6', '星期天']
# plt.xticks(x, week_info)
# plt.yticks(np.arange(-20, 40, 10))
#
# for i, j in zip(x, y):
#     plt.text(i, j + 1.5, "%dC" % (j))
#
# plt.legend(['最高温度', '最低温度'])
#
# # 3、显示、保存图
# plt.show()

# 二、散点图
plt.scatter(x, y)
# plt.show()

# 三、雷达图
angles= np.linspace(0, 2*np.pi, 5, endpoint=False)
label = np.array(["生存评分", "输出评分", "团战评分", "KDA", "发育评分"])
data = np.array([2,3.5,4,4.5,5])
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
plt.polar(angles, data)
plt.xticks(angles, label)
plt.show()