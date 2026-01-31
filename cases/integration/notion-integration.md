# Notion 集成案例

## 场景
使用 ClawBot 集成 Notion 笔记和数据库

## 配置

```bash
# 获取 Notion API Key
# https://www.notion.so/my-integrations

export NOTION_API_KEY="secret_xxx"
export NOTION_DATABASE_ID="database_id"
```

## 创建页面

```bash
# 创建页面
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "parent": {"database_id": "$NOTION_DATABASE_ID"},
    "properties": {
      "Name": {
        "title": [
          {"text": {"content": "新页面标题"}}
        ]
      },
      "Tags": {
        "multi_select": [
          {"name": "重要"}
        ]
      }
    },
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [
            {"text": {"content": "这是页面内容"}}
          ]
        }
      }
    ]
  }'
```

## 数据库操作

### 查询数据库

```bash
# 查询数据库
curl -X POST https://api.notion.com/v1/databases/$NOTION_DATABASE_ID/query \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "filter": {
      "property": "Tags",
      "multi_select": {
        "contains": "重要"
      }
    },
    "sorts": [
      {
        "property": "创建时间",
        "direction": "descending"
      }
    ]
  }'
```

### 更新页面

```bash
# 更新页面属性
curl -X PATCH https://api.notion.com/v1/pages/$PAGE_ID \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "properties": {
      "状态": {
        "select": {"name": "已完成"}
      }
    }
  }'
```

### 添加内容

```bash
# 添加块内容
curl -X PATCH https://api.notion.com/v1/blocks/$PAGE_ID/children \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "children": [
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
          "rich_text": [{"text": {"content": "二级标题"}}]
        }
      },
      {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
          "rich_text": [{"text": {"content": "列表项 1"}}]
        }
      }
    ]
  }'
```

## Notion 自动化

```bash
# 每日任务同步
write file_path:"~/notion-sync.sh" content:"

```bash
#!/bin/bash

# 获取今天的任务
TASKS=$(curl -s -X POST \"https://api.notion.com/v1/databases/$DATABASE_ID/query\" \
  -H \"Authorization: Bearer $NOTION_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -H \"Notion-Version: 2022-06-28\" \
  -d '{
    \"filter\": {
      \"and\": [
        {\"property\": \"状态\", \"select\": {\"does_not_equal\": \"完成\"}},
        {\"property\": \"截止日期\", \"date\": {\"equals\": \"'$(date +%Y-%m-%d)'\"}}
      ]
    }
  }' | jq -r '.results[] | \"- \" + .properties.Name.title[0].text.content')

if [ -n \"$TASKS\" ]; then
  echo \"今日任务：\"
  echo \"$TASKS\"
  # 发送到飞书
  curl -X POST \"$FEISHU_WEBHOOK\" \
    -H \"Content-Type: application/json\" \
    -d \"{\\\"msg_type\\\": \\\"text\\\", \\\"content\\\": {\\\"text\\\": \\\"今日任务：\\n$TASKS\\\"}}\"
fi
```

"
```

## 文件位置
`cases/integration/notion-integration.md`
