# OpenClaw/ClawDBot 资料大全

> 收集日期: 2026-01-30

---

## 📋 目录

1. [项目概述](#项目概述)
2. [官方资源](#官方资源)
3. [核心概念](#核心概念)
4. [安装配置](#安装配置)
5. [通道Channels](#通道channels)
6. [技能Skills](#技能skills)
7. [插件Plugins](#插件plugins)
8. [工具集](#工具集)
9. [高级功能](#高级功能)
10. [常见问题](#常见问题)
11. [社区生态](#社区生态)

---

## 项目概述

### 什么是 OpenClaw？

**OpenClaw** 是一个运行在你自己设备上的个人 AI 助手。它通过你已经使用的聊天渠道（WhatsApp、Telegram、Slack、Discord 等）与你交流，支持语音和文字，可以在 macOS/iOS/Android 上运行，并提供一个可控制的实时 Canvas 界面。

### 核心理念

- 🦞 **Space Lobster** - OpenClaw 的吉祥物是一只太空龙虾
- **本地优先** - 数据保存在本地，注重隐私
- **多通道统一** - 一个助手对接多个聊天平台
- **可扩展** - 通过 Skills 和 Plugins 扩展功能

### 创建者

- **Peter Steinberger** (@steipete) - 创建者，龙虾 whisperer
- **Mario Zechner** (@badlogic) - Pi creator，安全渗透测试

---

## 官方资源

### 官方网站

| 资源 | 地址 |
|------|------|
| **官网** | https://openclaw.ai |
| **文档** | https://docs.openclaw.ai |
| **GitHub** | https://github.com/openclaw/openclaw |
| **Discord** | https://discord.com/invite/clawd |
| **ClawdHub** | https://clawdhub.com (技能市场) |

### 核心命令

```bash
# 安装 CLI
npm install -g openclaw@latest

# 运行向导（推荐）
openclaw onboard --install-daemon

# 启动 Gateway
openclaw gateway --port 18789 --verbose

# 查看帮助
openclaw --help

# 打开控制台
openclaw dashboard
```

---

## 核心概念

### Gateway（网关）

Gateway 是 OpenClaw 的核心服务：
- 单进程运行，负责所有通道连接
- WebSocket 控制平面 (ws://127.0.0.1:18789)
- 本地默认绑定 127.0.0.1
- 支持远程访问（SSH 隧道或 Tailscale）

### Sessions（会话）

- **主会话 (main)** - 直接聊天，默认合并
- **群组隔离** - 每个群组独立会话
- **激活模式** - 可配置 always 或 mention 触发

### 多代理路由

可配置将不同通道/用户路由到不同的代理：
```json
{
  "routing": {
    "agents": {
      "main": {
        "workspace": "~/.openclaw/workspace",
        "sandbox": { "mode": "off" }
      }
    }
  }
}
```

### 网络模型

```
WhatsApp / Telegram / Discord / iMessage (+ plugins)
    │
    ▼
┌───────────────────────────┐
│ Gateway                   │
│ ws://127.0.0.1:18789      │
└───────────┬───────────────┘
            │
    ├─ Pi agent (RPC)
    ├─ CLI (openclaw …)
    ├─ Chat UI (SwiftUI)
    ├─ macOS app
    ├─ iOS node
    └─ Android node
```

---

## 安装配置

### 系统要求

- **Node.js** >= 22 (推荐)
- **pnpm** (可选，但推荐用于构建)
- **macOS**: Xcode / CLT (仅构建 App 需要)
- **Windows**: WSL2 (强烈推荐)

### 安装步骤

```bash
# 1. 安装 CLI
npm install -g openclaw@latest

# 2. 运行向导
openclaw onboard --install-daemon

# 3. 启动 Gateway
openclaw gateway --port 18789 --verbose

# 4. 验证安装
openclaw status
openclaw health
openclaw security audit --deep
```

### 从源码安装（开发）

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build
pnpm build
openclaw onboard --install-daemon

# 开发模式（自动重载）
pnpm gateway:watch
```

### 配置说明

配置文件位置：`~/.openclaw/openclaw.json`

示例配置：
```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123"],
      "groups": { "*": { "requireMention": true } }
    }
  },
  "messages": {
    "groupChat": { "mentionPatterns": ["@openclaw"] }
  }
}
```

---

## 通道Channels

OpenClaw 支持多种聊天平台，每个通道通过 Gateway 连接。

### 内置通道

| 通道 | 协议 | 特点 |
|------|------|------|
| **WhatsApp** | Baileys | 最流行，需要 QR 配对 |
| **Telegram** | Bot API (grammY) | DMs + 群组，Bot Token |
| **Discord** | Bot API | DMs + 服务器 + 频道 |
| **Slack** | Bolt SDK | 工作区应用 |
| **Google Chat** | HTTP Webhook | Google Chat API |
| **Signal** | signal-cli | 注重隐私 |
| **iMessage** | imsg CLI | macOS 原生 |
| **WebChat** | WebSocket | 本地 Web UI |

### 插件通道（需单独安装）

| 通道 | 说明 |
|------|------|
| **Mattermost** | Bot API + WebSocket |
| **BlueBubbles** | iMessage 推荐方案 |
| **Microsoft Teams** | Bot Framework |
| **LINE** | LINE Messaging API |
| **Matrix** | Matrix 协议 |
| **Nextcloud Talk** | 自托管聊天 |
| **Nostr** | 去中心化 DMs |
| **Zalo / Zalo Personal** | 越南常用 |
| **Twitch** | IRC 连接 |
| **Tlon** | Urbit 协议 |
| **飞书 (Feishu)** | 中国常用（插件） |

### 通道配置示例

#### Telegram 配置

```bash
# 设置 Bot Token
openclaw config set channels.telegram.botToken "YOUR_BOT_TOKEN"

# 启用
openclaw config set channels.telegram.enabled true

# 配置策略
openclaw config set channels.telegram.dmPolicy "pairing"
openclaw config set channels.telegram.groupPolicy "allowlist"

# 重启
openclaw gateway restart
```

#### 飞书配置（插件）

```bash
# 安装插件
openclaw plugins install @m1heng-clawd/feishu

# 配置凭证
openclaw config set channels.feishu.appId "cli_xxxxx"
openclaw config set channels.feishu.appSecret "your_secret"

# 启用
openclaw config set channels.feishu.enabled true
```

### DM 安全策略

| 策略 | 说明 |
|------|------|
| **pairing** | 未知发送者收到配对码，需审批 |
| **open** | 开放，任意用户可对话 |
| **allowlist** | 仅白名单用户可对话 |

### 群组策略

| 策略 | 说明 |
|------|------|
| **open** | 开放群组 |
| **allowlist** | 仅白名单群组 |
| **disabled** | 禁用群组 |

---

## 技能Skills

Skills 是 AgentSkills 兼容的技能文件夹，用于教会代理使用工具。

### 技能位置和优先级

技能从三个位置加载（优先级从高到低）：
1. **Workspace skills** - `/skills`
2. **Managed/local skills** - `~/.openclaw/skills`
3. **Bundled skills** - 安装包自带

### 技能格式

每个技能是一个包含 `SKILL.md` 的目录：

```markdown
---
name: weather
description: Get current weather and forecasts
metadata: {"openclaw":{"emoji":"🌤️","requires":{"anyBins":["curl"]}}}
---

# Weather Skill

Use this skill to get weather information...

## Usage

Just ask about the weather!
```

### 元数据字段

| 字段 | 说明 |
|------|------|
| `name` | 技能名称 |
| `description` | 描述 |
| `metadata.openclaw.emoji` | UI 显示的 emoji |
| `metadata.openclaw.os` | 适用的操作系统 |
| `metadata.openclaw.requires.bins` | 需要的二进制文件 |
| `metadata.openclaw.requires.env` | 需要的环境变量 |
| `metadata.openclaw.requires.config` | 需要的配置项 |
| `metadata.openclaw.homepage` | 官网链接 |
| `metadata.openclaw.install` | 安装器配置 |

### 技能配置

在 `~/.openclaw/openclaw.json` 中配置：

```json
{
  "skills": {
    "entries": {
      "weather": {
        "enabled": true,
        "apiKey": "WEATHER_API_KEY"
      },
      "github": {
        "enabled": true
      }
    }
  }
}
```

### ClawdHub（技能市场）

ClawdHub 是 OpenClaw 的公共技能仓库：

```bash
# 浏览技能
clawdhub

# 安装技能
clawdhub install

# 更新所有技能
clawdhub update --all

# 同步发布更新
clawdhub sync --all
```

### 常用技能列表

| 技能 | 描述 | 状态 |
|------|------|------|
| 🌤️ **weather** | 天气查询（无需 API Key） | ✅ |
| 🐙 **github** | GitHub 操作（Issue, PR, CI） | ✅ |
| 🧩 **coding-agent** | 编程助手（Codex, Claude Code） | ✅ |
| 📦 **skill-creator** | 创建自定义技能 | ✅ |
| ♊️ **gemini** | Gemini CLI 集成 | ✅ |
| 📦 **bluebubbles** | BlueBubbles 插件管理 | ✅ |
| 📝 **notion** | Notion API | ❌ |
| 💎 **obsidian** | Obsidian  vaults | ❌ |
| 📋 **trello** | Trello 管理 | ❌ |
| 🐦 **bird** | X/Twitter CLI | ❌ |

---

## 插件Plugins

Plugins 是扩展 OpenClaw 功能的包，可以添加新通道和技能。

### 插件管理

```bash
# 安装插件
openclaw plugins install @m1heng-clawd/feishu

# 列出已安装插件
openclaw plugins list

# 卸载插件
openclaw plugins uninstall feishu
```

### 飞书插件（clawd-feishu）

#### 安装

```bash
npm install @m1heng-clawd/feishu
# 或
openclaw plugins install @m1heng-clawd/feishu
```

#### 配置

1. 在[飞书开放平台](https://open.feishu.cn)创建自建应用
2. 获取 App ID 和 App Secret
3. 开启权限：
   - `contact:user.base:readonly`
   - `im:message`
   - `im:message.p2p_msg:readonly`
   - `im:message.group_at_msg:readonly`
   - `im:message:send_as_bot`
   - `im:resource`
4. 配置事件订阅（选择**长连接**）：
   - `im.message.receive_v1`
   - `im.message.message_read_v1`
   - `im.chat.member.bot.added_v1`
   - `im.chat.member.bot.deleted_v1`

#### 插件配置

```bash
openclaw config set channels.feishu.appId "cli_xxxxx"
openclaw config set channels.feishu.appSecret "your_secret"
openclaw config set channels.feishu.enabled true
```

#### 配置选项

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxxxx",
      "appSecret": "secret",
      "domain": "feishu",  // 或 "lark"
      "connectionMode": "websocket",  // 或 "webhook"
      "dmPolicy": "pairing",  // pairing | open | allowlist
      "groupPolicy": "allowlist",  // open | allowlist | disabled
      "requireMention": true,
      "mediaMaxMb": 30,
      "renderMode": "auto"  // auto | raw | card
    }
  }
}
```

---

## 工具集

OpenClaw 提供了丰富的工具供 AI 使用。

### 核心工具

| 工具 | 功能 |
|------|------|
| **exec** | 执行 shell 命令 |
| **read** | 读取文件 |
| **write** | 写入文件 |
| **edit** | 编辑文件 |
| **browser** | 浏览器控制 |
| **canvas** | Canvas 渲染 |
| **nodes** | 节点控制 |
| **message** | 发送消息 |
| **cron** | 定时任务 |
| **memory** | 记忆管理 |

### 高级工具

| 工具 | 功能 |
|------|------|
| **web_search** | 网页搜索（需 Brave API Key） |
| **web_fetch** | 获取网页内容 |
| **image** | 图片分析 |
| **tts** | 文字转语音 |
| **sessions** | 会话管理 |
| **agents** | 多代理管理 |
| **gateway** | Gateway 控制 |
| **process** | 后台进程管理 |

---

## 高级功能

### 1. 多代理路由

将不同用户/通道路由到不同的工作空间：

```json
{
  "routing": {
    "agents": {
      "main": { "workspace": "~/.openclaw/workspace" },
      "work": { "workspace": "~/work-agent" }
    }
  }
}
```

### 2. 沙盒模式

安全地执行危险操作：

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "non-main"  // main 之外都沙盒
      }
    }
  }
}
```

### 3. 远程访问

#### SSH 隧道
```bash
ssh -L 18789:localhost:18789 user@host
```

#### Tailscale Serve
```bash
openclaw gateway --bind tailnet --token YOUR_TOKEN
```

### 4. 定时任务 (Cron)

```bash
# 添加任务
openclaw cron add --name "每日提醒" --schedule "0 9 * * *" \
  --payload "提醒我写日报"

# 列出任务
openclaw cron list

# 运行任务
openclaw cron run <jobId>
```

### 5. Webhooks

自动化回调：

```bash
# 创建 webhook
openclaw webhooks create --url https://example.com/callback
```

### 6. 语音功能

#### Voice Wake（语音唤醒）
- macOS 菜单栏应用支持
- iOS/Android 节点支持
- 使用 ElevenLabs TTS

#### Talk Mode（对话模式）
- 实时语音对话
- 支持 macOS/iOS/Android

### 7. Live Canvas

AI 驱动的可视化工作空间：
- 支持 A2UI 推送/重置
- 可截图和评估
- 跨平台支持

### 8. 节点控制

```bash
# 列出节点
openclaw nodes list

# 节点状态
openclaw nodes status <nodeId>

# 相机控制
openclaw nodes camera_snap --node <nodeId>

# 屏幕录制
openclaw nodes screen_record --node <nodeId>
```

---

## 常见问题

### Q1: 机器人收不到消息？

1. 检查 Gateway 状态：`openclaw gateway status`
2. 检查通道配置：`openclaw config get channels`
3. 查看日志：`openclaw logs`
4. **飞书用户**：确认事件订阅已配置（长连接模式）

### Q2: 如何开始新对话？

发送 `/new` 命令即可开启新对话。

### Q3: 如何清理历史记录？

```bash
# 删除对话
openclaw sessions delete <sessionKey>

# 重置配置
openclaw reset
```

### Q4: 飞书机器人找不到？

1. 确认应用已发布到测试版本
2. 在飞书搜索框中搜索机器人名称
3. 检查应用可用范围是否包含你的账号

### Q5: 如何更新 OpenClaw？

```bash
# 更新 CLI
openclaw update run

# 重启 Gateway
openclaw gateway restart

# 切换通道
openclaw update --channel stable|beta|dev
```

### Q6: 消息不是流式输出？

飞书 API 有频率限制，当前采用完整回复后一次性发送的方式。

### Q7: Windows 上无法运行？

- **强烈推荐使用 WSL2** (Ubuntu)
- 原生 Windows 未经过测试，兼容性差

### Q8: 沙盒无法运行？

- 确认 Docker 已安装
- 检查 `agents.defaults.sandbox.docker.setupCommand`
- 某些包安装需要网络和 root 权限

---

## 社区生态

### Discord 社区

- **服务器**: `https://discord.com/invite/clawd`
- **频道**: 讨论、帮助、分享、 Showcase

### ClawdHub（技能市场）

- **网址**: https://clawdhub.com
- **功能**: 浏览、安装、同步、发布技能

### 贡献者

| 贡献者 | 贡献内容 |
|--------|---------|
| **Maxim Vovshin** (@Hyaxia) | Blogwatcher 技能 |
| **Nacho Iacovino** (@nachoiacovino) | 位置解析 (Telegram + WhatsApp) |
| **m1heng** | 飞书插件 |

### 许可证

MIT License - 免费开源 🦞

---

## 附录

### 命令速查

| 操作 | 命令 |
|------|------|
| 启动 Gateway | `openclaw gateway start` |
| 重启 Gateway | `openclaw gateway restart` |
| 查看状态 | `openclaw health` |
| 查看配置 | `openclaw config get --json` |
| 发送消息 | `openclaw message send --message "Hello"` |
| 诊断问题 | `openclaw doctor` |
| 查看日志 | `openclaw logs` |
| 安装插件 | `openclaw plugins install <name>` |
| 安装技能 | `openclaw skills install <name>` |
| 控制台 UI | `openclaw dashboard` |

### 文件位置

| 文件/目录 | 位置 |
|----------|------|
| 配置文件 | `~/.openclaw/openclaw.json` |
| 工作空间 | `~/.openclaw/workspace/` |
| 技能目录 | `~/.openclaw/skills/` |
| 扩展目录 | `~/.openclaw/extensions/` |
| 日志 | `/tmp/openclaw/openclaw-*.log` |

### 开发通道

| 通道 | 版本 | 说明 |
|------|------|------|
| **stable** | vYYYY.M.D | 正式版，npm latest |
| **beta** | vYYYY.M.D-beta.N | 预发布，npm beta |
| **dev** | main HEAD | 开发版，npm dev |

切换通道：`openclaw update --channel stable|beta|dev`

---

## 参考链接汇总

### 官方文档
- 主页: https://docs.openclaw.ai
- 入门: https://docs.openclaw.ai/start/getting-started
- 向导: https://docs.openclaw.ai/start/wizard
- 通道: https://docs.openclaw.ai/channels
- 技能: https://docs.openclaw.ai/tools/skills
- 安全: https://docs.openclaw.ai/gateway/security

### GitHub
- 主仓库: https://github.com/openclaw/openclaw
- 飞书插件: https://github.com/m1heng/clawdbot-feishu
- Nix 打包: https://github.com/openclaw/nix-clawdbot

### 社区
- Discord: https://discord.com/invite/clawd
- ClawdHub: https://clawdhub.com

### 平台支持
- macOS: https://docs.openclaw.ai/platforms/macos
- iOS: https://docs.openclaw.ai/platforms/ios
- Android: https://docs.openclaw.ai/platforms/android
- Windows: https://docs.openclaw.ai/platforms/windows

---

*文档最后更新: 2026-01-30*
*由 ClawDBot 自动整理生成 🦞*
