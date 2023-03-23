import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 读取文件
aa =r'../data/fl4.xls'
df = pd.DataFrame(pd.read_excel(aa))
df1=df['label1'].drop_duplicates().values.tolist()
df2=df[['label1','label2','weight']]

#设置画布大小
plt.figure(figsize=(6, 5))
#颜色数据
colors = df['color'].drop_duplicates().values.tolist()

G = nx.Graph()
# 添加边
for i in df2.index:
    G.add_edge(df2.label1[i], df2.label2[i], weight=df2.weight[i])
# 定义两个边，并给边赋予权重，其中u是起点，v是终点，d是权重
edge1 = [(u, v) for (u, v, d) in G.edges(data=True) if (d['weight'] >=1)]
edge2 = [(u, v) for (u, v, d) in G.edges(data=True) if (d['weight'] >=15)]

# 图的布局
# 节点在一个圆环上均匀分布
pos = nx.circular_layout(G)
#用Fruchterman-Reingold算法排列节点
#pos=nx.spring_layout(G)
#节点随机分布
#pos=nx.spring_layout(G)

# 点
nx.draw_networkx_nodes(G, pos, alpha=1, node_size=200,node_color=colors,node_shape='o')
#nx.draw_networkx_nodes(G, pos, alpha=1, node_size=300,node_color=colors,node_shape='p')
# 边
nx.draw_networkx_edges(G, pos, edgelist=edge1,width=1, alpha=0.3, edge_color='g', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=edge2, width=1.5, alpha=0.5, edge_color='red')
# 标签
nx.draw_networkx_labels(G, pos, font_size=9)
# 生成结果
plt.axis('off')
plt.title('《复仇者联盟4》人物关系图')
plt.rcParams['font.size'] = 10
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.show()
