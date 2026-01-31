# 飞书集成案例

## 场景
ClawBot 与飞书的深度集成

## 配置飞书

```bash
# 安装飞书插件
openclaw plugins install @m1heng-clawd/feishu

# 配置凭证
openclaw config set channels.feishu.appId "cli_xxxxx"
openclaw config set channels.feishu.appSecret "your_secret"
openclaw config set channels.feishu.enabled true

# 重启 Gateway
openclaw gateway restart
```

## 飞书功能使用

### 1. 私聊对话

```
用户: 你好

ClawBot: 你好！有什么可以帮你的？
```

### 2. 群聊 @机器人

```
用户: @ClawBot 帮我查一下天气

ClawBot: 🌤️ 今日天气：晴，温度 15-25°C
```

### 3. 发送富文本消息

```bash
# 发送卡片消息
message action:send channel:feishu message:"## 项目更新\n\n✅ 任务完成"
```

### 4. 处理文件

```bash
# 发送图片
message action:send channel:feishu media:"~/screenshot.png"

# 发送文档
message action:send channel:feishu filePath:"~/report.pdf"
```

## 高级功能

### 消息卡片

```json
{
  "type": "card",
  "elements": [
    {
      "type": "section",
      "text": {
        "type": "markdown",
        "content": "**任务状态更新**"
      }
    }
  ]
}
```

### 交互式卡片

```json
{
  "type": "card",
  "elements": [
    {
      "type": "action",
      "actions": [
        {
          "type": "button",
          "text": "批准",
          "value": "approve"
        }
      ]
    }
  ]
}
```

## 文件位置
`cases/integration/feishu-integration.md`
