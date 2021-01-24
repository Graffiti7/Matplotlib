import matplotlib.pyplot as plt
import random
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(20,8),dpi=80)
figure,axes = plt.subplots(nrows=1,ncols=2,figsize=(20,8),dpi = 80)
x = range(60)

y_beijing = [random.uniform(15,18) for i in x]

y_shanghai = [random.uniform(25,28) for i in x]

plt.plot(x,y_beijing,color = "r",linestyle = "--",label="北京")

plt.plot(x,y_shanghai,color = "b",linestyle = "-",label="上海")

#显示图例
plt.legend()
#修改x y轴刻度
x_label = ["11时{}分".format(i) for i in x]

plt.xticks(x[::5],x_label[::5])
plt.yticks(range(0,40,5)) 

#增加网格(是否显示，网格样式，透明度)
plt.grid(True,linestyle="--",alpha = 0.5)

#添加标题
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("温度变化图示")

plt.show()