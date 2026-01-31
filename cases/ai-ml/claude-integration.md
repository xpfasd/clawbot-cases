# Claude AI 集成案例

## 场景
使用 ClawBot 调用 Anthropic Claude AI 服务

## API 配置

```bash
# 获取 API Key
# https://console.anthropic.com/

export ANTHROPIC_API_KEY="sk-ant-api03-xxx"
```

## 基础调用

### Claude 3 Opus

```bash
# 调用 Claude 3 Opus
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-opus-20240229\",
    \"prompt\": \"Human: 用 Python 写一个简单的 Web 服务器\\n\\nAssistant:\",
    \"max_tokens_to_sample\": 2000,
    \"temperature\": 0.7
  }'
```

"
```

### Claude 3 Sonnet

```bash
# 调用 Claude 3 Sonnet（更快更便宜）
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-sonnet-20240229\",
    \"prompt\": \"Human: 解释什么是 RESTful API\\n\\nAssistant:\",
    \"max_tokens_to_sample\": 1000,
    \"temperature\": 0.5
  }'
```

"
```

### Claude 3 Haiku

```bash
# 调用 Claude 3 Haiku（最快）
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-haiku-20240307\",
    \"prompt\": \"Human: 你好\\n\\nAssistant:\",
    \"max_tokens_to_sample\": 500,
    \"temperature\": 0.3
  }'
```

"
```

## Messages API

```bash
# 使用新的 Messages API
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/messages \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-5-sonnet-20241022\",
    \"max_tokens\": 1024,
    \"messages\": [
      {\"role\": \"user\", \"content\": \"用 Python 写一个快速排序\"}
    ]
  }'
```

"
```

## 系统提示词

```bash
# 使用系统提示词
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/messages \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-5-sonnet-20241022\",
    \"max_tokens\": 1024,
    \"system\": \"你是一个 Python 专家，擅长编写高质量的 Python 代码。\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"写一个装饰器用于函数重试\"}
    ]
  }'
```

"
```

## 流式响应

```bash
# 流式响应
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/messages \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -H \"Accept: text/event-stream\" \
  -d '{
    \"model\": \"claude-3-5-sonnet-20241022\",
    \"max_tokens\": 500,
    \"messages\": [
      {\"role\": \"user\", \"content\": \"写一首关于春天的诗\"}
    ]
  }'
```

"
```

## 多模型对比工具

```bash
# 对比 Claude 和 GPT-4
write file_path:"~/compare-models.sh" content:"

```bash
#!/bin/bash

QUESTION=\"什么是量子计算？\"

echo \"=== Claude 3 Opus ===\"
curl -s -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $ANTHROPIC_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d \"{\\"model\\": \\"claude-3-opus-20240229\\", \\"prompt\\": \\"Human: $QUESTION\\\\n\\\\nAssistant:\\", \\"max_tokens_to_sample\\": 500}\" | \
  jq -r '.completion'

echo \"\"
echo \"=== GPT-4 ===\"
curl -s -X POST https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d \"{\\"model\\": \\"gpt-4\\", \\"messages\\": [{\\"role\\": \\"user\\", \\"content\\": \\"$QUESTION\\"}]}\" | \
  jq -r '.choices[0].message.content'
```

"
```

## 定价对比

| 模型 | 输入 ($/1M tokens) | 输出 ($/1M tokens) |
|------|-------------------|-------------------|
| Claude 3 Opus | $15.00 | $75.00 |
| Claude 3 Sonnet | $3.00 | $15.00 |
| Claude 3 Haiku | $0.25 | $1.25 |
| Claude 3.5 Sonnet | $3.00 | $15.00 |

## 文件位置
`cases/ai-ml/claude-integration.md`
