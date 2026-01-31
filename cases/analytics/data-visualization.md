# 数据可视化案例

## 场景
使用 ClawBot 创建数据可视化图表

## Matplotlib

### 基本图表

```python
import matplotlib.pyplot as plt
import numpy as np

# 折线图
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('正弦函数')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('sin.png', dpi=150)
```

### 多子图

```python
# 创建 2x2 子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图 1
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3])
axes[0, 0].set_title('子图 1')

# 子图 2
axes[0, 1].bar([1, 2, 3], [3, 7, 5])
axes[0, 1].set_title('子图 2')

# 子图 3
axes[1, 0].scatter([1, 2, 3, 4], [4, 3, 2, 1])
axes[1, 0].set_title('子图 3')

# 子图 4
axes[1, 1].pie([30, 20, 50], labels=['A', 'B', 'C'])
axes[1, 1].set_title('子图 4')

plt.tight_layout()
plt.savefig('subplots.png', dpi=150)
```

## Plotly（交互式图表）

```python
import plotly.express as px
import pandas as pd

# 交互式散点图
df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

fig = px.scatter(df, x='x', y='y', color='category',
                 title='交互式散点图')
fig.show()
fig.write_html('scatter.html')

# 交互式折线图
fig = px.line(df, x='x', y='y', title='交互式折线图')
fig.write_html('line.html')
```

## 数据仪表板

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 创建仪表板
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('销售额', '用户增长', '转化率', '满意度'),
    specs=[[{"type": "bar"}, {"type": "line"}],
           [{"type": "indicator"}, {"type": "pie"}]]
)

# 添加图表
fig.add_trace(
    go.Bar(x=['1月', '2月', '3月'], y=[100, 150, 130]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=['1月', '2月', '3月'], y=[1000, 1500, 2000]),
    row=1, col=2
)

fig.add_trace(
    go.Indicator(mode=\"number+delta\", value=75, number={'suffix': '%'}),
    row=2, col=1
)

fig.add_trace(
    go.Pie(values=[30, 20, 50], labels=['满意', '一般', '不满意']),
    row=2, col=2
)

fig.update_layout(height=800, title_text=\"数据仪表板\")
fig.write_html('dashboard.html')
```

## 热力图

```python
import seaborn as sns

# 相关性热力图
data = np.random.rand(10, 10)
sns.heatmap(data, annot=True, cmap='coolwarm', center=0)
plt.title('相关性热力图')
plt.savefig('heatmap.png', dpi=150)
```

## 地图可视化

```python
import plotly.express as px

# 地图散点
df = pd.DataFrame({
    'lat': [39.9, 31.2, 22.5, 34.0],
    'lon': [116.4, 121.5, 114.1, 118.3],
    'city': ['北京', '上海', '深圳', '杭州'],
    'value': [100, 80, 60, 70]
})

fig = px.scatter_geo(df, lat='lat', lon='lon',
                     size='value', hover_name='city',
                     title='城市数据分布')
fig.update_geos(projection_type=\"natural earth\")
fig.write_html('map.html')
```

## 文件位置
`cases/analytics/data-visualization.md`
