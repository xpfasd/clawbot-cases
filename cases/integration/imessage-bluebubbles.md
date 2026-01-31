# iMessage 集成案例

## 场景
使用 ClawBot 通过 BlueBubbles 发送 iMessage

## BlueBubbles 配置

```bash
# 安装 BlueBubbles
# https://bluebubbles.app/

# 配置连接
export BLUEBUBBLES_URL="http://localhost:1234"
export BLUEBUBBLES_PASSWORD="your_password"
```

## 发送消息

### 发送文本

```bash
# 发送文本消息
curl -X POST "$BLUEBUBBLES_URL/api/v1/message/text" \
  -H "Content-Type: application/json" \
  -H "password: $BLUEBUBBLES_PASSWORD" \
  -d '{
    "recipient": "+1234567890",
    "message": "Hello from ClawBot!"
  }'
```

### 发送图片

```bash
# 发送图片
curl -X POST "$BLUEBUBBLES_URL/api/v1/message/attachment" \
  -H "password: $BLUEBUBBLES_PASSWORD" \
  -F "recipient=+1234567890" \
  -F "attachment=@/path/to/image.jpg"
```

### 发送群组消息

```bash
# 发送群组消息（使用 GUID）
curl -X POST "$BLUEBUBBLES_URL/api/v1/message/text" \
  -H "Content-Type: application/json" \
  -H "password: $BLUEBUBBLES_PASSWORD" \
  -d '{
    "guid": "iMessage;+1234567890;+0987654321",
    "message": "群发消息"
  }'
```

## 获取消息

```bash
# 获取最新消息
curl -X GET "$BLUEBUBBLES_URL/api/v1/message/recent?limit=20" \
  -H "password: $BLUEBUBBLES_PASSWORD"

# 获取特定聊天
curl -X GET "$BLUEBUBBLES_URL/api/v1/chat/guid:iMessage;+1234567890" \
  -H "password: $BLUEBUBBLES_PASSWORD"
```

## 聊天管理

```bash
# 创建群聊
curl -X POST "$BLUEBUBBLES_URL/api/v1/chat/create" \
  -H "Content-Type: application/json" \
  -H "password: $BLUEBUBBLES_PASSWORD" \
  -d '{
    "participants": ["+1234567890", "+0987654321"],
    "message": "欢迎加入群聊"
  }'

# 获取聊天列表
curl -X GET "$BLUEBUBBLES_URL/api/v1/chat" \
  -H "password: $BLUEBUBBLES_PASSWORD"
```

## 文件位置
`cases/integration/imessage-bluebubbles.md`
