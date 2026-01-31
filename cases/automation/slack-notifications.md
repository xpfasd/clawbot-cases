# Slack 通知案例

## 场景
使用 ClawBot 发送 Slack 通知

## 配置 Slack 通道

```bash
# 安装 Slack 技能
openclaw skills install slack

# 配置 Token
openclaw config set channels.slack.botToken "xoxb-your-token"
openclaw config set channels.slack.enabled true

# 重启 Gateway
openclaw gateway restart
```

## 发送通知

### 基础消息

```bash
# 发送文本消息
message action:send channel:slack target:"#general" message:"Hello Slack!"
```

### 格式化消息

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*项目更新*\n✅ 任务已完成"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "mrkdwn",
          "text": "由 ClawBot 自动发送"
        }
      ]
    }
  ]
}
```

### 添加附件

```json
{
  "attachments": [
    {
      "color": "#36a64f",
      "title": "部署完成",
      "text": "项目已成功部署到生产环境",
      "fields": [
        {
          "title": "环境",
          "value": "production",
          "short": true
        },
        {
          "title": "耗时",
          "value": "5分钟",
          "short": true
        }
      ],
      "footer": "ClawBot",
      "ts": 1234567890
    }
  ]
}
```

## 自动化通知

### Cron 定时报告

```bash
# 添加每日报告任务
openclaw cron add \
  --name "每日Slack报告" \
  --schedule "0 9 * * 1-5" \
  --payload "向 #reports 频道发送每日报告"
```

### GitHub 集成

```bash
# GitHub Actions 通知
message action:send channel:slack target:"#github" message:":github: CI/CD 完成\n✅ 构建成功"
```

### 错误告警

```bash
# 发送错误通知
message action:send channel:slack target:"#alerts" message::warning: *系统错误*\n错误信息: {error_message}
```

## Slack Block Kit

### 按钮

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "任务处理完成"
      },
      "accessory": {
        "type": "button",
        "text": {
          "type": "plain_text",
          "text": "查看详情"
        },
        "url": "https://example.com/task/123"
      }
    }
  ]
}
```

### 选择器

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "选择操作"
      },
      "accessory": {
        "type": "static_select",
        "placeholder": {
          "type": "plain_text",
          "text": "选择操作"
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "批准"
            },
            "value": "approve"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "拒绝"
            },
            "value": "reject"
          }
        ]
      }
    }
  ]
}
```

## 最佳实践

1. **使用渠道正确性** - 区分 #alerts 和 #general
2. **避免刷屏** - 控制通知频率
3. **格式化清晰** - 使用 Block Kit 丰富内容
4. **设置免打扰** - 考虑用户时区

## 文件位置
`cases/automation/slack-notifications.md`
