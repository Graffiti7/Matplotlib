import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

movie_name = ["雷神3","正义联盟","蝙蝠侠"]
y = [73853,57767,22354]

#创建画布
plt.figure(figsize=(20,8),dpi=100)

#绘制饼图
plt.pie(y,labels=movie_name,colors=["r","b","y"],autopct="%1.2f%%")

#显示图例
plt.legend()

#保持圆形
plt.axis('equal')
plt.show()