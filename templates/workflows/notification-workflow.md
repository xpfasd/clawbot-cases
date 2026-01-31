# 通知工作流模板

## 场景
通用通知自动化工作流

## 模板结构

```json
{
  "name": "notification-workflow",
  "description": "通用通知工作流模板",
  "version": "1.0.0",
  "type": "notification",
  "channels": ["slack", "feishu", "telegram"],
  "triggers": [
    {
      "type": "cron",
      "config": {
        "schedule": "0 9 * * *"
      }
    },
    {
      "type": "webhook",
      "config": {
        "path": "/notify"
      }
    }
  ],
  "templates": {
    "slack": {
      "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "*通知*"
          }
        }
      ]
    },
    "feishu": {
      "type": "card",
      "content": "**通知**"
    }
  }
}
```

## 使用场景

1. **定时报告** - 每日/每周总结
2. **告警通知** - 系统错误告警
3. **状态更新** - 任务状态变更
4. **事件提醒** - 会议/截止日期提醒

## 文件位置
`templates/workflows/notification-workflow.md`
