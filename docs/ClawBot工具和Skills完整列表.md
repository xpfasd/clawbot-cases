# ClawBot 可安装工具和 Skills 完整列表

> ClawBot 工具和技能大全

---

## 📋 目录

1. [Skills 技能列表](#skills-技能列表)
2. [CLI 命令列表](#cli-命令列表)
3. [插件列表](#插件列表)
4. [安装指南](#安装指南)

---

## 🧩 Skills 技能列表

ClawBot 提供 **49 个** 可安装技能，目前已就绪 **6 个**。

### ✅ 已就绪（可立即使用）

| 技能 | 描述 | 命令/工具 |
|------|------|----------|
| 📦 **bluebubbles** | BlueBubbles iMessage 插件管理 | iMessage 通道 |
| 🧩 **coding-agent** | AI 编程助手（Codex/Claude Code） | codex exec |
| ♊️ **gemini** | Gemini CLI 集成 | gemini |
| 🐙 **github** | GitHub 操作（Issue/PR/CI） | gh |
| 📦 **skill-creator** | 创建自定义技能 | skill-creator |
| 🌤️ **weather** | 天气查询（无需 API Key） | 天气 |

### 📝 生产效率类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 📝 **apple-notes** | Apple Notes 管理（macOS） | `memo` CLI |
| ⏰ **apple-reminders** | Apple 提醒事项管理 | `remindctl` CLI |
| 🐻 **bear-notes** | Bear 笔记管理 | grizzly CLI |
| 💎 **obsidian** | Obsidian  vaults 管理 | obsidian-cli |
| 📋 **trello** | Trello 看板管理 | Trello API |
| ✅ **things-mac** | Things 3 任务管理 | things CLI |

### 💬 通讯社交类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 🐦 **bird** | Twitter/X CLI | cookies |
| 💬 **slack** | Slack 控制 | slack CLI |
| 📱 **wacli** | WhatsApp 消息 | wacli CLI |
| 📧 **himalaya** | 邮箱管理（IMAP/SMTP） | himalaya CLI |

### 🎨 媒体娱乐类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 🖼️ **openai-image-gen** | OpenAI 图像生成 | DALL-E API |
| 🎙️ **openai-whisper** | 本地语音转文字 | Whisper CLI |
| ☁️ **openai-whisper-api** | API 语音转文字 | Whisper API |
| 🗣️ **sag** | ElevenLabs TTS | sag CLI |
| 🎵 **spotify-player** | Spotify 控制 | spogo |
| 🔊 **sonoscli** | Sonos 音箱控制 | sonoscli |
| 🧲 **gifgrep** | GIF 搜索 | gifgrep |
| 🌊 **songsee** | 音频可视化 | songsee CLI |

### 🔐 安全密码类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 🔐 **1password** | 1Password CLI | op CLI |

### 🏠 智能家居类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 🫐 **blucli** | BluOS 音箱控制 | blu CLI |
| 💡 **openhue** | Philips Hue 灯控 | openhue CLI |
| 🎛️ **eightctl** | Eight Sleep 温度控制 | eightctl CLI |

### 📍 位置地图类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 📍 **goplaces** | Google Places 搜索 | goplaces CLI |
| 📍 **local-places** | 本地地点搜索 | Google API |

### 📊 数据分析类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 📊 **model-usage** | 模型使用成本统计 | codexbar CLI |
| 🧾 **summarize** | 文本/视频摘要 | summarize CLI |
| 📰 **blogwatcher** | RSS/博客监控 | blogwatcher CLI |
| 📜 **session-logs** | 会话日志分析 | jq |

### 🎮 开发工具类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 📦 **clawdhub** | ClawdHub 技能市场 | clawdhub CLI |
| 🧿 **oracle** | Oracle CLI 最佳实践 | oracle CLI |
| 📦 **mcporter** | MCP 服务器工具 | mcporter CLI |
| 🛵 **ordercli** | 外卖订单查询 | Foodora CLI |
| 🧵 **tmux** | tmux 远程控制 | tmux |

### 🎞️ 视频图像类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 📸 **camsnap** | 相机帧捕获（RTSP/ONVIF） | 相机 API |
| 🎞️ **video-frames** | 视频帧提取 | ffmpeg |
| 📄 **nano-pdf** | PDF 编辑 | nano-pdf CLI |
| 🍌 **nano-banana-pro** | Gemini 图像生成 | Nano Banana API |

### 🤖 AI 相关类

| 技能 | 描述 | 需安装 |
|------|------|--------|
| 👀 **peekaboo** | macOS UI 自动化 | Peekaboo CLI |
| 📞 **voice-call** | 语音通话 | voice-call 插件 |

---

## 🖥️ CLI 命令列表

### 基础命令

| 命令 | 描述 |
|------|------|
| `openclaw --version` | 查看版本 |
| `openclaw --help` | 查看帮助 |
| `openclaw dashboard` | 打开控制台 UI |
| `openclaw doctor` | 健康检查 |

### 配置管理

| 命令 | 描述 |
|------|------|
| `openclaw config get <path>` | 获取配置 |
| `openclaw config set <path> <value>` | 设置配置 |
| `openclaw config unset <path>` | 删除配置 |

### Gateway 管理

| 命令 | 描述 |
|------|------|
| `openclaw gateway start` | 启动 Gateway |
| `openclaw gateway stop` | 停止 Gateway |
| `openclaw gateway restart` | 重启 Gateway |
| `openclaw gateway status` | 查看状态 |
| `openclaw logs` | 查看日志 |

### 通道管理

| 命令 | 描述 |
|------|------|
| `openclaw channels list` | 列出通道 |
| `openclaw channels login` | 登录通道 |
| `openclaw doctor` | 诊断通道问题 |

### 消息管理

| 命令 | 描述 |
|------|------|
| `openclaw message send` | 发送消息 |
| `openclaw message delete` | 删除消息 |
| `openclaw message edit` | 编辑消息 |

### 插件管理

| 命令 | 描述 |
|------|------|
| `openclaw plugins list` | 列出插件 |
| `openclaw plugins install <name>` | 安装插件 |
| `openclaw plugins uninstall <name>` | 卸载插件 |

### 技能管理

| 命令 | 描述 |
|------|------|
| `openclaw skills list` | 列出技能 |
| `openclaw skills install <name>` | 安装技能 |
| `openclaw skills show <name>` | 查看技能详情 |

### 自动化

| 命令 | 描述 |
|------|------|
| `openclaw cron list` | 列出定时任务 |
| `openclaw cron add` | 添加定时任务 |
| `openclaw cron rm` | 删除定时任务 |
| `openclaw cron run <id>` | 运行定时任务 |

### 节点管理

| 命令 | 描述 |
|------|------|
| `openclaw nodes list` | 列出节点 |
| `openclaw nodes status <node>` | 节点状态 |
| `openclaw nodes camera_snap` | 相机拍照 |
| `openclaw nodes screen_record` | 屏幕录制 |

### 会话管理

| 命令 | 描述 |
|------|------|
| `openclaw sessions list` | 列出会话 |
| `openclaw sessions history <key>` | 会话历史 |
| `openclaw sessions send <key>` | 发送消息 |

### 系统工具

| 命令 | 描述 |
|------|------|
| `openclaw memory search <query>` | 搜索记忆 |
| `openclaw browse start` | 启动浏览器 |
| `openclaw sandbox` | 沙盒工具 |
| `openclaw acp` | Agent Control Protocol |

---

## 🔌 插件列表

ClawBot 支持 **30 个** 插件，目前已加载 **3 个**。

### ✅ 已加载（可立即使用）

| 插件 | 描述 |
|------|------|
| **Feishu** | 飞书通道（我们已配置） |
| **Telegram** | Telegram 通道 |
| **Memory (Core)** | 记忆核心模块 |

### 💬 消息通道插件

| 插件 | 描述 |
|------|------|
| **whatsapp** | WhatsApp 通道 |
| **discord** | Discord 通道 |
| **slack** | Slack 通道 |
| **googlechat** | Google Chat 通道 |
| **imessage** | iMessage 通道 |
| **signal** | Signal 通道 |
| **matrix** | Matrix 协议 |
| **mattermost** | Mattermost 通道 |
| **msteams** | Microsoft Teams |
| **line** | LINE 通道 |
| **nextcloud-talk** | Nextcloud Talk |
| **nostr** | Nostr DMs |
| **tlon** | Tlon/Urbit |
| **twitch** | Twitch 聊天 |
| **zalo** | Zalo 通道 |
| **zalouser** | Zalo 个人账户 |

### 🔐 认证插件

| 插件 | 描述 |
|------|------|
| **google-antigravity-auth** | Google OAuth |
| **google-gemini-cli-auth** | Gemini CLI OAuth |
| **qwen-portal-auth** | 通义千问 OAuth |

### 🧠 AI 相关插件

| 插件 | 描述 |
|------|------|
| **bluebubbles** | BlueBubbles iMessage |
| **copilot-proxy** | Copilot 代理 |
| **llm-task** | LLM 任务工具 |
| **lobster** | 工作流工具 |

### 🔧 工具插件

| 插件 | 描述 |
|------|------|
| **memory-lancedb** | LanceDB 长期记忆 |
| **diagnostics-otel** | 诊断/遥测 |
| **voice-call** | 语音通话 |
| **open-prose** | Prose 写作技能 |

---

## 📦 安装指南

### 安装 Skills

```bash
# 使用 ClawdHub
npx clawdhub

# 或手动安装
openclaw skills install <skill-name>
```

### 安装插件

```bash
# 安装飞书插件（已安装）
openclaw plugins install @m1heng-clawd/feishu

# 安装 WhatsApp 插件
openclaw plugins install @openclaw/whatsapp

# 安装 Discord 插件
openclaw plugins install @openclaw/discord
```

### 启用插件

```bash
# 启用插件
openclaw config set channels.feishu.enabled true

# 重启 Gateway
openclaw gateway restart
```

---

## 🎯 常用组合推荐

### 编程开发
- coding-agent + github + skill-creator

### 日常办公
- github + weather + apple-notes + apple-reminders

### 社交沟通
- telegram + slack + imessage

### 内容创作
- openai-image-gen + sag + openai-whisper

### 智能家居
- openhue + blucli + eightctl

---

## 📊 统计概览

| 类别 | 数量 |
|------|------|
| **Skills 技能** | 49 个（6 个就绪） |
| **CLI 命令** | 40+ 个 |
| **插件** | 30 个（3 个加载） |

---

*文档生成时间: 2026-01-30*
*由 ClawDBot 🦞 整理*
