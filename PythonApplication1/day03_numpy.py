import numpy as np

"""
安装了anaconda，在pycharm 中import numpy 不成功的。
1、cmd中 输入python-------import numpy
2、如果成功，设置pycharm的setting

其他方法安装：cmd------输入：pip install numpy
"""


# 一、创建数组
# 1、array函数,可以传入列表、元组。
arr1 = np.array([1, 2, 3])
# print(arr1)

# arr2 = np.array([[1, 2, 3],
#                  [2, 3, 1]
#                  ])
# print(arr2)

# 二、数组的属性
# shape、ndim、dtype、size、itemsize
# 使用方法：数组名.属性名
# print(arr2.shape)  # 返回数组的形状，行、列。元组的形式
# print(arr2.ndim)
# print(arr2.dtype)  # 数组中元素的类型
# print(arr2.size)  # 数据中 所有元素
# print(arr2.itemsize)  #  --->8 每个元素的字节数。 1个字节=X位  64位的float/8位=

# 重点：一维数组 没有行列的概念。只有一个元素的元组（元素1，）
# print("arr1.shape:-----{}".format(arr1.shape))  # -->(3,)  (1,3)X

# 创建数组2 ----特殊函数
# start stop step(默认1)
arr3 = np.arange(1, 11, 3)  # 从1到10  前闭后开[a, b)
# print(arr3)

# 全0 2行3列
arr4 = np.zeros(shape=(2, 3), dtype=int)
# print(arr4)

# np.eye 对角数组（矩阵）, 1单位数组（矩阵）。
arr5 = np.eye(3)
# print(arr5)

# 对角矩阵
arr6 = np.diag([1, 2, 3])
# print(arr6)

arr7 =np.logspace(0, 2, num=3)  # base 10    # [0, 1, 2]
# print(arr7)

# 随机数 种子 seed  可复现性
np.random.seed(0)
arr8 = np.random.random((2, 3)) # 传入的shape
# print(arr8)

# 四、数据访问: 下标法、切片法 (前闭后开)
# arr2 = np.array([[1, 2, 3],
#                  [2, 3, 1],
#                  [3, 2, 1],
#                  [4, 5, 6]
#                  ])

# print(arr2[0, 1])
# print(arr2[0, 0:2])

# 取出所有行第一列
# print(arr2[0:5, 0])
# bool_index = arr2[0:5, 0]%2== 0
# print(bool_index)
#
# bool_index1 = np.array([1, 0, 2], dtype=bool)
# print(bool_index1)
# bool 索引的长度 必须和行、列的长度相等
# print(arr2[:, bool_index1])  # bool 索引

# 五、数组的变形
# 1、一维数组到二维数组、二维数组到1维，二维到二维
arr2 = np.array([[1, 2, 3],
                 [2, 3, 1],
                 [3, 2, 1],
                 [4, 5, 6]
                 ])

# 1、直接使用shape属性
# arr2.shape = (12,)  # 行优先访问
# print(arr2)

# 2、reshapes函数. 不就地修改.建议大家用reshape
arr9 = arr2.reshape(12,)
# print(arr9)
# print(arr2)

# -1占位符号，元素个数/2
# 变形必须保证 总size一致
# arr10 = np.arange(1, 9).reshape(2, -1)
# print(arr10)

# flatten 函数，如果修改一维数组 不会改变原始的高维数组。
# ravel 函数 如果修改一维数组 会改变原始的高维数组。
arr11 = np.random.random((2,3))
# print(arr11)
# arr12 = arr11.flatten()
arr12 = arr11.ravel()  # 展平为1维数组
# print(arr12)
arr12[0] = 100
# print('*'*60)
# print(arr11)
# print(arr12)

# 六、矩阵的创建
mat1 = np.mat(arr2)
# print(mat1)
# print(type(mat1))
# print(type(arr2))

mat2 = np.mat('1 2 3; 2 3 1')
# print(mat2)
# print(mat2.T)
# print(type(mat2.A))
mat3 = np.mat([[1, 1, 1],
               [2, 2, 2]])
# print(mat3)

# 矩阵的运算：加法、减法。 操作的矩阵shape是一致的
# print(mat2 + mat3)
# # print(mat2.shape)
# print('-'*60)
# print(np.multiply(mat2, mat3))
# print(mat2*mat3) 需要遵守数学里的矩阵乘法的规则

# 数组和矩阵是可以相互转换的。
# mat.A----> 对应的数组
# np.mat(数组) -----对应的矩阵

# 七、数组的运算：算术运算（+、-、*、**）、逻辑运算和比较运算
arr13 = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
arr14 = np.array([[1, 2],
                  [2, 4]])
# 算术运算（+、-、*、**, /） 要求：操作的数组 shape必须一致
# print(arr13 * arr14)
# 数组的关系 运算 就是。数组中对应位置元素的运算
# print(arr13 == arr14)

# print(np.all(arr13 == arr14))  # and 是否所有元素都XX
# print(np.any(arr13 == arr14))  # or 是否存在元素XX

# print(np.all(arr13>3))

# arr13是一个2行3列的。3只是一个值

# 数组的广播机制

# 一维数组 充当 列的位置
arr15 = np.array([2, 3, 3])
# print(arr15.shape)
# print(arr15.ndim)

# 八、数组的读写:。二进制文件
# 单个数组的读写 save、load
# 保存数组时，默认后缀为npy
np.save("数组arr15", arr15)
# 读npy文件中，必须加后缀
new_arr = np.load("数组arr15.npy")
# print(new_arr)

# 多个数组的读写
# 后缀为npz，保存时 默认为字典的形式，key为arr_X[0,1,------]
np.savez("多个数组", arr14=arr14, arr15=arr15)
new_arrs = np.load("多个数组.npz")
# print(new_arrs)
# for i in new_arrs:
#     print(i)
#     print(new_arrs[i])

# 默认保存的是浮点数
np.savetxt("数组.txt", arr14, fmt="%d")

# 九、数组的统计分析
# sort函数，就地修改
arr16 = np.array([1, 2, 3, 6, 5, 4])
# print(arr16)
# arr16.sort()
# print(arr16)
# 排序默认是递增的，默认是axis=1
arr17 = arr16.reshape(3, 2)
# print(arr17)
# print('*'*60)
# arr17.sort(axis=1)
# print(arr17)

# 返回的排序元素的下标值
sort_index = arr16.argsort() # 0 1 2 5 4 3
# print(arr16[sort_index[:4]])

# unique 对数组进行去重，并排序
arr18 = np.array([4,1,2,3,1,2,2,1,1,1,1,1])
# print(np.unique(arr18))


arr16 = np.array([1, 2, 3, 6, 5, 4])
# print(np.max(arr16))
# print(np.sum(arr16))
arr17 = arr16.reshape(3, 2)
# print(arr17)
# print(np.max(arr17, axis=1))

# print(np.sum(arr16))
# print(np.cumsum(arr16))

# （1）员工的平均薪资为多少？
# （2）公司任职最久的员工是谁？
# （3）员工的平均工作年限是多少？
# （4）员工总体流失率是多少？
# （5）员工整体满意程度如何？

data_info = np.load("lol_data.npz")
data = data_info["data"]
cloumns = data_info["cloumns"]
# print(cloumns)
# ['工号' '姓名' '部门' '岗位' '薪资' '工龄' '满意度' '状态']
print(data.shape)
salary = data[:, 4].astype(int)
print("员工的平均薪资为{0}".format(np.mean(salary)))

years = data[:,5].astype(int)
print("员工的平均年限为{0}".format(np.mean(years)))

max_year = np.min(years)  # ----- 10
bool_index = years == max_year  #   谁的工作年限为10
print(bool_index)
print("工作最短的是：", data[bool_index, 1][0])




