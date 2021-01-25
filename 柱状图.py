import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
movie_name = ["雷神3","正义联盟","蝙蝠侠"]

y = [73853,57767,22354]

plt.figure(figsize=(20,8),dpi=80)

x_ticks = range(len(movie_name))

plt.bar(x_ticks,y,color = ["r","b","y"])

plt.xticks(x_ticks,movie_name)

plt.title("票房对比")

plt.grid(linestyle="--")

plt.show()