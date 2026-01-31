# 数据管道工作流模板

## 场景
自动化数据处理管道

## 模板结构

```json
{
  "name": "data-pipeline",
  "description": "数据采集、处理、存储管道",
  "version": "1.0.0",
  "type": "pipeline",
  "steps": [
    {
      "name": "fetch-data",
      "type": "http",
      "config": {
        "url": "https://api.example.com/data",
        "method": "GET"
      },
      "output": "rawData"
    },
    {
      "name": "transform-data",
      "type": "processor",
      "config": {
        "script": "transform.js"
      },
      "input": "rawData",
      "output": "cleanData"
    },
    {
      "name": "store-data",
      "type": "database",
      "config": {
        "operation": "insert",
        "table": "records"
      },
      "input": "cleanData"
    },
    {
      "name": "notify-completion",
      "type": "notification",
      "config": {
        "channels": ["slack"],
        "message": "数据处理完成：{recordsCount} 条记录"
      }
    }
  ],
  "schedule": {
    "cron": "0 */6 * * *",
    "tz": "Asia/Shanghai"
  },
  "errorHandling": {
    "onError": "notify",
    "retry": {
      "maxAttempts": 3,
      "delay": 300
    }
  }
}
```

## 步骤类型

| 类型 | 说明 |
|------|------|
| http | HTTP 请求 |
| processor | 数据处理 |
| database | 数据库操作 |
| notification | 通知发送 |
| file | 文件操作 |

## 文件位置
`templates/workflows/data-pipeline-workflow.md`
