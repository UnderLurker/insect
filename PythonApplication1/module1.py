import matplotlib.pyplot as plt
import numpy as np
#x = np.arange(1, 8)  # [1,2,3..7]
#y = np.array([15, 20, 22, 23, 20, 18, 16])
#y1=y-5
#plt.rcParams['font.sans-serif']='SimHei'
#plt.rcParams['axes.unicode_minus']=False
#plt.figure()
##plt.plot(x,y,marker='o',linestyle='--')
##plt.plot(x,y1,marker='o',linestyle='--')
#plt.scatter(x,y)
#plt.scatter(x,y1)
#plt.title('hhhhhhhhh')
#plt.xlabel('日期')
#plt.ylabel('温度')
#week_info =['星期1', '星期2', '星期2', '星期3', '星期4', '星期5', '星期6', '星期天']
#plt.xticks(x,week_info)
#plt.yticks(np.arange(-20,40,10))
#for i,j in zip(x,y):
#    plt.text(i,j+1.5,'%d℃'%j)
#plt.legend(['最高温度','最低温度'])
#plt.show()
angles=np.linspace(0,2*np.pi,6,endpoint=False)
label=np.array([1,2,3,4,5,6])
data=np.array([7,7,7,7,7,7])
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
plt.polar(angles,data)
plt.xticks(angles,label)
plt.show()