import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

data = pd.read_csv('company.csv',encoding='ansi')
train_data = data.iloc[:,-2:]
k = 5
km = KMeans(k,random_state=1)
km.fit(train_data)
y_pred = km.predict(train_data)
print(y_pred)
train_data.loc[:,'类别'] = y_pred
plt.figure()
for i in range(k):
    bool_index = train_data.loc[:,'类别'] == i
    x = train_data.loc[bool_index,'平均每次消费金额']
    y = train_data.loc[bool_index,'平均消费周期（天）']
    plt.scatter(x,y)
plt.show()

