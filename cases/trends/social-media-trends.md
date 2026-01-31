# 社交媒体趋势案例

## 场景
获取和分析社交媒体平台的热搜趋势

## Twitter/X 趋势

### API 配置

```bash
# 获取 Twitter API 凭证
# https://developer.twitter.com

export TWITTER_BEARER_TOKEN="your_bearer_token"
```

### 获取趋势

```bash
# 获取全球趋势
bash command:"

```sh
curl \"https://api.twitter.com/2/trends/place.json?id=1\" \
  -H \"Authorization: Bearer $TWITTER_BEARER_TOKEN\"
```

"

# 获取特定地区趋势
bash command:"

```sh
# 23424977 = 中国
# 23424977 = United States
curl \"https://api.twitter.com/2/trends/place.json?id=23424977\" \
  -H \"Authorization: Bearer $TWITTER_BEARER_TOKEN\"
```

"
```

### 搜索推文

```bash
# 搜索特定关键词的推文
bash command:"

```sh
curl \"https://api.twitter.com/2/tweets/search/recent?query=OpenClaw&tweet.fields=created_at,author_id\" \
  -H \"Authorization: Bearer $TWITTER_BEARER_TOKEN\"
```

"
```

## Reddit 趋势

### 获取热门帖子

```bash
# 获取热门帖子
bash command:"

```sh
# 所有板块热门
curl \"https://www.reddit.com/r/all/top.json?limit=10&t=day\" \
  -H \"User-Agent: ClawBot/1.0\"

# 技术板块
curl \"https://www.reddit.com/r/programming/top.json?limit=10&t=day\" \
  -H \"User-Agent: ClawBot/1.0\"

# AI 板块
curl \"https://www.reddit.com/r/ArtificialIntelligence/top.json?limit=10&t=day\" \
  -H \"User-Agent: ClawBot/1.0\"
```

"
```

### 搜索帖子

```bash
# 搜索相关帖子
bash command:"

```sh
curl \"https://www.reddit.com/search.json?q=AI+news&sort=hot&limit=10\" \
  -H \"User-Agent: ClawBot/1.0\"
```

"
```

## 微博热搜

```bash
# 获取微博热搜
bash command:"

```sh
# 使用第三方 API 或爬虫
curl -s \"https://weibo.com/ajax/statuses/mymblog?uid=0&feature=0&is_search=0&key_word=热搜\" | jq '.list[].text_raw'
```

"
```

## TikTok 趋势

```bash
# TikTok 热门话题（需要官方 API）
bash command:"

```sh
# 第三方数据源
curl -s \"https://api.tiktokapi.com/trending\"
```

"
```

## 多平台趋势聚合

```bash
# 聚合多平台趋势
write file_path:"~/aggregate-trends.sh" content:"

```bash
#!/bin/bash

echo \"=== Twitter 趋势 ===\"
curl -s \"https://api.twitter.com/2/trends/place.json?id=1\" \
  -H \"Authorization: Bearer $TWITTER_BEARER_TOKEN\" | \
  jq -r '.[] | .trends[] | .name' | head -5

echo \"\"
echo \"=== Reddit 热门 ===\"
curl -s \"https://www.reddit.com/r/all/top.json?limit=5&t=day\" \
  -H \"User-Agent: ClawBot/1.0\" | \
  jq -r '.data.children[].data.title' | head -5

echo \"\"
echo \"=== Google 趋势 ===\"
python3 get_google_trends.py | head -5
```

"
```

## 趋势分析

```bash
# 趋势情感分析
write file_path:"~/sentiment-analysis.py" content:"

```python
import json
from collections import Counter

# 收集各平台讨论
discussions = []

# Twitter
tw_data = get_twitter_discussions(\"AI\")
discussions.extend(tw_data)

# Reddit
rd_data = get_reddit_discussions(\"AI\")
discussions.extend(rd_data)

# 情感分析
from textblob import TextBlob

sentiments = []
for text in discussions:
    blob = TextBlob(text)
    sentiments.append({
        'text': text[:100],
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity
    })

# 统计
positive = sum(1 for s in sentiments if s['polarity'] > 0)
negative = sum(1 for s in sentiments if s['polarity'] < 0)
neutral = len(sentiments) - positive - negative

print(f\"正面: {positive}, 负面: {negative}, 中性: {neutral}\")
```

"
```

## 文件位置
`cases/trends/social-media-trends.md`
