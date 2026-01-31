# 关键词研究案例

## 场景
使用 ClawBot 进行 SEO 关键词研究和分析

## 关键词分析

### 基础查询

```bash
# 使用 Google Trends 分析关键词
write file_path:"~/keyword-analysis.py" content:"

```python
from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='zh-CN', tz=360)

# 定义关键词列表
keywords = [
    '人工智能',
    '机器学习',
    '深度学习',
    'ChatGPT',
    'AI助手'
]

# 获取趋势数据
pytrends.build_payload(
    kw_list=keywords,
    timeframe='today 12-m',
    geo='CN'
)

# 趋势对比
interest_over_time = pytrends.interest_over_time()

# 按地区
interest_by_region = pytrends.interest_by_region()

# 相关查询
related_queries = pytrends.related_queries()

# 保存数据
interest_over_time.to_csv('keyword_trends.csv')

print(\"关键词趋势数据已保存\")
print(interest_over_time.tail())
```

"
```

### 关键词建议

```bash
# 发现相关关键词
write file_path:"~/find-keywords.py" content:"

```python
from pytrends.request import TrendReq
import json

pytrends = TrendReq()

seed_keywords = ['AI', '人工智能']

for keyword in seed_keywords:
    pytrends.build_payload(kw_list=[keyword])
    related = pytrends.related_queries()
    
    if keyword in related:
        rising = related[keyword].get('rising', [])
        top = related[keyword].get('top', [])
        
        print(f\"\\n=== {keyword} 相关关键词 ===\")
        print(\"上升趋势:\")
        for item in rising[:10]:
            print(f\"  {item['query']}: {item['value']}\")
        print(\"热门:\")
        for item in top[:10]:
            print(f\"  {item['query']}: {item['value']}\")
```

"
```

## SEO 分析

### 竞争对手分析

```bash
# 分析竞争对手网站
write file_path:"~/competitor-analysis.sh" content:"

```bash
#!/bin/bash
SITE=\"$1\"

# 获取页面标题
echo \"页面标题:\"
curl -s \"$SITE\" | grep -o '<title>[^<]*</title>' | sed 's/<[^>]*>//g'

# 获取 Meta 描述
echo \"\\nMeta 描述:\"
curl -s \"$SITE\" | grep -o 'meta name=\"description\" content=\"[^\"]*\"' | sed 's/.*content=\"\\([^\"]*\\)\".*/\\1/'

# 获取 H1 标签
echo \"\\nH1 标签:\"
curl -s \"$SITE\" | grep -o '<h1[^>]*>[^<]*</h1>' | sed 's/<[^>]*>//g'

# 检查关键词密度
echo \"\\n检查关键词密度...\"
python3 analyze_density.py \"$SITE\"
```

"
```

### 排名追踪

```bash
# 追踪关键词排名
write file_path:"~/rank-tracker.py" content:"

```python
import requests
from bs4 import BeautifulSoup
import time

def check_google_ranking(keyword, site):
    \"\"\"检查网站在 Google 中的排名\"\"\"
    url = f\"https://www.google.com/search?q={keyword}&hl=zh-CN\"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = soup.find_all('div', class_='g')
    for i, result in enumerate(results, 1):
        if site in result.get_text():
            return i
    
    return None

# 追踪
keywords = ['ClawBot', 'OpenClaw']
site = 'github.com/openclaw'

for kw in keywords:
    rank = check_google_ranking(kw, site)
    print(f\"关键词 '{kw}': 排名 #{rank}\" if rank else f\"关键词 '{kw}': 未找到\")
    time.sleep(2)
```

"
```

## 内容优化

### 关键词优化建议

```bash
# 生成优化建议
write file_path:"~/content-optimizer.py" content:"

```python
class SEOOptimizer:
    def __init__(self, content, target_keyword):
        self.content = content
        self.keyword = target_keyword
    
    def analyze(self):
        return {
            'keyword_density': self._calculate_density(),
            'keyword_position': self._find_positions(),
            'title_optimization': self._check_title(),
            'meta_description': self._check_meta(),
            'headings': self._check_headings(),
            'suggestions': self._generate_suggestions()
        }
    
    def _calculate_density(self):
        words = len(self.content.split())
        keyword_count = self.content.lower().count(self.keyword.lower())
        return (keyword_count / words * 100) if words > 0 else 0
    
    def _find_positions(self):
        text = self.content.lower()
        keyword = self.keyword.lower()
        return [i for i in range(len(text)) if text.startswith(keyword, i)]
    
    def _check_title(self):
        return {
            'has_title': '<h1' in self.content.lower() or '<title>' in self.content.lower(),
            'keyword_in_title': self.keyword.lower() in self.content.lower()
        }
    
    def _generate_suggestions(self):
        suggestions = []
        analysis = self.analyze()
        
        if analysis['keyword_density'] < 0.5:
            suggestions.append(\"增加关键词密度\")
        if not analysis['title_optimization']['keyword_in_title']:
            suggestions.append(\"在标题中添加关键词\")
        
        return suggestions

# 使用
optimizer = SEOOptimizer(content, \"人工智能\")
result = optimizer.analyze()
print(json.dumps(result, ensure_ascii=False, indent=2))
```

"
```

## 文件位置
`cases/trends/keyword-research.md`
