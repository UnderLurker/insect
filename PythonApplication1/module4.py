import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

#读取表格
data = pd.read_excel('nba1.xls')
train_data = data.loc[:,['篮板数','助攻数','总分数']]
exp1 = train_data.loc[:,'篮板数'] == ' '
exp2 = train_data.loc[:,'助攻数'] == ' '
exp3 = train_data.loc[:,'总分数'] == ' '
bool_index = exp1 | exp2 | exp3
#series转list
list1 = bool_index.tolist()
count = 0
list2 = []
for i in list1:
    if i:
        list2.append(count)
    count+=1
#删除dataframe中有空格的行
train_data.drop(list2,inplace=True)
#KMeans算法
k = 5
km = KMeans(k,random_state=1)
km.fit(train_data)
y_pred = km.predict(train_data)
train_data.loc[:,'类别'] = y_pred
#打印每行的聚类中心
print(y_pred)

#画雷达图
angles = np.linspace(0,2 * np.pi,5,endpoint=False)
label = ['控球后卫','得分后卫','小前锋','大前锋','中锋']#计数器s1 s2 s3 s4 s5
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
s=[]
for i in range(k):
    #统计分布情况
    bool_index = train_data.loc[:,'类别'] == i
    count=0
    for i in bool_index.tolist():
        if i:
            count+=1
    s.append(count)
s=np.array(s)
s=np.concatenate((s,[s[0]]))
angles=np.concatenate((angles,[angles[0]]))
plt.polar(angles,s)
plt.xticks(angles,label)
plt.title('NBA球员位置分析')
plt.fill(angles,s,alpha=0.25)
plt.grid(True)
plt.show()

