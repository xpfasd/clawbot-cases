# Google API 集成案例

## 场景
使用 ClawBot 集成各种 Google 服务

## Google Gemini API

### 配置

```bash
# 获取 API Key
# 访问 https://aistudio.google.com/app/apikey

# 配置环境变量
export GEMINI_API_KEY="your_api_key"
```

### 文本生成

```bash
# Gemini Pro
bash command:"

```sh
curl -X POST \"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GEMINI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"contents\": [{
      \"parts\": [{\"text\": \"用 Python 写一个快速排序\"}]
    }],
    \"generationConfig\": {
      \"temperature\": 0.7,
      \"maxOutputTokens\": 1000
    }
  }'
```

"
```

### 图片理解

```bash
# Gemini Pro Vision
bash command:"

```sh
curl -X POST \"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=$GEMINI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"contents\": [{
      \"parts\": [
        {\"text\": \"描述这张图片的内容\"},
        {\"inline_data\": {
          \"mime_type\": \"image/jpeg\",
          \"data\": \"'$(base64 -w0 image.jpg)'\"
        }}
      ]
    }]
  }'
```

"
```

## Google Search API

### 配置

```bash
# 安装自定义搜索 JSON API
# https://developers.google.com/custom-search/v1/overview

export GOOGLE_SEARCH_API_KEY="your_api_key"
export GOOGLE_SEARCH_CX="your_cx_id"
```

### 搜索

```bash
# Web 搜索
bash command:"

```sh
curl \"https://www.googleapis.com/customsearch/v1?key=$GOOGLE_SEARCH_API_KEY&cx=$GOOGLE_SEARCH_CX&q=OpenClaw\"
```

"

# 图片搜索
bash command:"

```sh
curl \"https://www.googleapis.com/customsearch/v1?key=$GOOGLE_SEARCH_API_KEY&cx=$GOOGLE_SEARCH_CX&q=cute+cat&searchType=image\"
```

"
```

## Google Maps API

### 地点搜索

```bash
# 配置
export GOOGLE_MAPS_API_KEY="your_api_key"

# 搜索地点
bash command:"

```sh
curl \"https://maps.googleapis.com/maps/api/place/textsearch/json?query= restaurants+in+San+Francisco&key=$GOOGLE_MAPS_API_KEY\"
```

"

# 获取详情
bash command:"

```sh
curl \"https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJw6BwuF2H5zs&key=$GOOGLE_MAPS_API_KEY\"
```

"
```

## Google Drive API

### 文件操作

```bash
# 列出文件
bash command:"

```sh
curl -X GET \"https://www.googleapis.com/drive/v3/files?pageSize=10&fields=files(id,name,mimeType)\" \
  -H \"Authorization: Bearer $GOOGLE_DRIVE_TOKEN\"
```

"

# 下载文件
bash command:"

```sh
curl -X GET \"https://www.googleapis.com/drive/v3/files/FILE_ID?alt=media\" \
  -H \"Authorization: Bearer $GOOGLE_DRIVE_TOKEN\" \
  -o output.txt
```

"
```

## Google Sheets API

### 读写数据

```bash
# 读取数据
bash command:"

```sh
curl \"https://sheets.googleapis.com/v4/spreadsheets/SPREADSHEET_ID/values/Sheet1!A1:E5?valueRenderOption=UNFORMATTED_VALUE&majorDimension=ROWS\" \
  -H \"Authorization: Bearer $GOOGLE_SHEETS_TOKEN\"
```

"

# 写入数据
bash command:"

```sh
curl -X PUT \"https://sheets.googleapis.com/v4/spreadsheets/SPREADSHEET_ID/values/Sheet1!A1\" \
  -H \"Authorization: Bearer $GOOGLE_SHEETS_TOKEN\" \
  -H \"Content-Type: application/json\" \
  -d '{\"values\": [[\"Name\", \"Age\"], [\"张三\", 25]]}'
```

"
```

## Google Calendar API

### 事件管理

```bash
# 创建事件
bash command:"

```sh
curl -X POST \"https://www.googleapis.com/calendar/v3/calendars/primary/events\" \
  -H \"Authorization: Bearer $GOOGLE_CALENDAR_TOKEN\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"summary\": \"团队会议\",
    \"description\": \"讨论项目进度\",
    \"start\": {
      \"dateTime\": \"2026-01-30T10:00:00+08:00\",
      \"timeZone\": \"Asia/Shanghai\"
    },
    \"end\": {
      \"dateTime\": \"2026-01-30T11:00:00+08:00\",
      \"timeZone\": \"Asia/Shanghai\"
    }
  }'
```

"

# 列出事件
bash command:"

```sh
curl \"https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=2026-01-30T00:00:00+08:00&maxResults=10\" \
  -H \"Authorization: Bearer $GOOGLE_CALENDAR_TOKEN\"
```

"
```

## Google Trends API

### 获取趋势数据

```bash
# 使用 pytrends 库
bash command:"

```bash
pip install pytrends

python3 << 'EOF'
from pytrends.request import TrendReq

pytrends = TrendReq(hl='zh-CN', tz=360)
pytrends.build_payload(
    kw_list=['OpenClaw', 'ChatGPT', 'AI助手']
)

# 兴趣随时间变化
interest_over_time = pytrends.interest_over_time()

# 兴趣按地区
interest_by_region = pytrends.interest_by_region()

# 相关主题
related_queries = pytrends.related_queries()

print(interest_over_time.head())
EOF
```

"
```

## 文件位置
`cases/integration/google-api-integration.md`
