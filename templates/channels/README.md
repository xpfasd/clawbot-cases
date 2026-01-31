# 通道配置模板索引

> 本目录包含所有通道配置模板

## 📂 目录结构

```
channels/
├── README.md              # 本索引文件
├── telegram.json          # Telegram 配置模板
├── whatsapp.json          # WhatsApp 配置模板
├── discord.json           # Discord 配置模板
├── slack.json             # Slack 配置模板
├── feishu.json            # 飞书配置模板
└── google-chat.json       # Google Chat 配置模板
```

## 🎯 模板列表

| 通道 | 协议 | 难度 | 特点 |
|------|------|------|------|
| Telegram | Bot API | ⭐ | 最简单，Bot Token |
| WhatsApp | Baileys | ⭐⭐ | 需要 QR 登录 |
| Discord | Bot API | ⭐ | Bot Token |
| Slack | Bolt SDK | ⭐⭐ | OAuth 配置 |
| 飞书 | Webhook | ⭐⭐ | App ID/Secret |
| Google Chat | HTTP | ⭐ | Webhook URL |

## 🔧 配置步骤

1. **获取凭证** - 从对应平台获取 API Key/Token
2. **配置 OpenClaw** - 使用 config set 命令
3. **重启 Gateway** - 使配置生效
4. **测试连接** - 发送测试消息

## 💡 选择建议

- **新手推荐**: Telegram（最简单）
- **国内用户**: 飞书
- **团队协作**: Slack/Discord

---

*由 ClawDBot 整理 🦞*
