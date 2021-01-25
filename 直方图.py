import matplotlib.pyplot as plt
import random


#准备数据
x = [random.randint(0,50) for i in range(250)]
#创建画布
plt.figure()
#绘制直方图(数据，组数，频率显示)
distance = 2
group_num = int((max(x)-min(x))/distance)
plt.hist(x,bins=group_num,density=True)
#修改x轴刻度
plt.xticks(range(min(x),max(x)+2,distance))
#添加网格
plt.grid(linestyle="--",alpha = 0.5)
#显示图像
plt.show()