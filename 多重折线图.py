import matplotlib.pyplot as plt
import random
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

#返回图对象与绘图区
figure,axes = plt.subplots(nrows=1,ncols=2,figsize=(20,8),dpi = 80)

#准备数据
x = range(60)

y_beijing = [random.uniform(15,18) for i in x]

y_shanghai = [random.uniform(25,28) for i in x]

#绘制图像
axes[0].plot(x,y_beijing,color = "r",linestyle = "--",label="北京")

axes[1].plot(x,y_shanghai,color = "b",linestyle = "-",label="上海")

#显示图例
axes[0].legend()
axes[1].legend()

#修改x y轴刻度
x_label = ["11时{}分".format(i) for i in x]

axes[0].set_xticks(x[::10])
axes[0].set_xticklabels(x_label[::10])
axes[0].set_yticks(range(0,40,5)) 
axes[1].set_xticks(x[::10])
axes[1].set_xticklabels(x_label[::10])
axes[1].set_yticks(range(0,40,5)) 

#增加网格(是否显示，网格样式，透明度)
axes[0].grid(True,linestyle="--",alpha = 0.5)
axes[1].grid(True,linestyle="--",alpha = 0.5)

#添加标题
axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].set_title("温度变化图示")
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].set_title("温度变化图示")

#显示图
plt.show()