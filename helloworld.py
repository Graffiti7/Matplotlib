import matplotlib.pyplot as plt


plt.figure(figsize=(10,8),dpi=80)#创建画布（canvas)

plt.plot([0,1,2,3,4,5,6],[1,2,3,4,5,6,7])#画图(plot)

plt.savefig("test1.png")#保存图像（要在show之前）

plt.show()#显示图像

