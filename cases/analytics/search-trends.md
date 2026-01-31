# 搜索与趋势分析案例

## 场景
使用 ClawBot 进行搜索和趋势分析

## Google 搜索

### 基础搜索

```bash
# 使用 curl 搜索
bash command:"

```sh
curl \"https://www.googleapis.com/customsearch/v1?key=$GOOGLE_SEARCH_API_KEY&cx=$GOOGLE_SEARCH_CX&q=人工智能发展趋势\"
```

"
```

### 搜索结果解析

```bash
# 解析搜索结果
write file_path:"~/parse-search.sh" content:"

```bash
#!/bin/bash
QUERY=\"$1\"

response=$(curl -s \"https://www.googleapis.com/customsearch/v1?key=$GOOGLE_SEARCH_API_KEY&cx=$GOOGLE_SEARCH_CX&q=$QUERY\")

# 提取标题和链接
echo \"$response\" | jq -r '.items[] | \"标题: \" + .title + \"\\n链接: \" + .link + \"\\n摘要: \" + (.snippet | .[0:100]) + \"\\n\"'
```

"
```

## 趋势数据分析

### Google Trends 数据获取

```bash
# 使用 pytrends 获取趋势数据
bash command:"

```bash
#!/bin/bash
pip install pytrends pandas matplotlib

python3 << 'EOF'
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='zh-CN', tz=360)

# 定义关键词
keywords = ['ChatGPT', 'OpenAI', 'Claude', 'AI助手']

# 构建负载
pytrends.build_payload(
    kw_list=keywords,
    timeframe='today 3-m',
    geo='CN'
)

# 随时间变化的兴趣
interest_over_time = pytrends.interest_over_time()

# 保存数据
interest_over_time.to_csv('trends_data.csv')

# 绘制图表
plt.figure(figsize=(12, 6))
for keyword in keywords:
    plt.plot(interest_over_time.index, interest_over_time[keyword], label=keyword)
plt.legend()
plt.title('AI 相关关键词趋势')
plt.xlabel('时间')
plt.ylabel('搜索热度')
plt.savefig('trends_chart.png')
print(\"趋势图表已保存\")
EOF
```

"
```

### 趋势对比

```bash
# 对比多个关键词
write file_path:"~/trend-comparison.py" content:"

```python
from pytrends.request import TrendReq
import json

pytrends = TrendReq()

# 比较关键词
kw_list = ['AI', '机器学习', '深度学习', 'ChatGPT']
pytrends.build_payload(kw_list=kw_list, timeframe='today 12-m')

# 相关主题
related = pytrends.related_queries()

# 按地区
region = pytrends.interest_by_region()

print(json.dumps(related, ensure_ascii=False, indent=2))
print(region.head(10))
```

"
```

## 社交媒体趋势

### Twitter/X 趋势

```bash
# 查看 Twitter 趋势
bash command:"

```sh
# 使用 Twitter API
curl \"https://api.twitter.com/2/trends/place.json?id=1\" \
  -H \"Authorization: Bearer $TWITTER_TOKEN\"
```

"
```

### Reddit 趋势

```bash
# 查看 Reddit 热门
bash command:"

```sh
curl \"https://www.reddit.com/r/all/top.json?limit=10\" \
  -H \"User-Agent: ClawBot/1.0\"
```

"
```

## 趋势报告生成

```bash
# 生成趋势报告
write file_path:"~/generate-trend-report.sh" content:"

```bash
#!/bin/bash

TOPIC=\"AI助手\"
OUTPUT_FILE=\"trend_report_$(date +%Y%m%d).md\"

cat > \"$OUTPUT_FILE\" << EOF
# $TOPIC 趋势分析报告

生成时间: $(date)

## 1. 搜索趋势

EOF

# 获取 Google Trends 数据
python3 get_trends.py \"$TOPIC\" >> \"$OUTPUT_FILE\"

cat >> \"$OUTPUT_FILE\" << EOF

## 2. 社交媒体讨论

EOF

# 获取 Reddit 讨论
curl -s \"https://www.reddit.com/search.json?q=$TOPIC&sort=hot&limit=5\" | \
  jq -r '.data.children[].data.title' >> \"$OUTPUT_FILE\"

cat >> \"$OUTPUT_FILE\" << EOF

## 3. 新闻报道

EOF

# 获取相关新闻
curl -s \"https://news.google.com/rss/search?q=$TOPIC\" | \
  grep -o '<title>.*</title>' | head -10 | \
  sed 's/<[^>]*>//g' >> \"$OUTPUT_FILE\"

echo \"报告已生成: $OUTPUT_FILE\"
```

"
```

## 数据可视化

```bash
# 创建交互式图表
write file_path:"~/visualize-trends.py" content:"

```python
import plotly.express as px
import pandas as pd

# 读取数据
df = pd.read_csv('trends_data.csv', index_col=0, parse_dates=True)

# 创建交互式图表
fig = px.line(df, x=df.index, y=df.columns, 
              title='AI 相关关键词搜索趋势',
              labels={'value': '搜索热度', 'index': '时间'})

fig.update_layout(hovermode='x unified')
fig.show()

# 保存为 HTML
fig.write_html('trends_interactive.html')
```

"
```

## 文件位置
`cases/analytics/search-trends.md`
