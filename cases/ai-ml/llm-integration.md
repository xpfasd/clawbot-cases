# AI/LLM 集成案例

## 场景
使用 ClawBot 调用各种 LLM 服务（GPT/Claude/Gemini 等）

## OpenAI GPT-4

### 基础调用

```bash
# 调用 GPT-4
bash command:"

```sh
curl -X POST https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"gpt-4\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"你是一个助手\},
      {\"role\": \"user\", \"content\": \"解释什么是机器学习\"}
    ],
    \"temperature\": 0.7,
    \"max_tokens\": 1000
  }'
```

"
```

### 函数调用

```json
{
  "messages": [...],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "获取天气信息",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "城市名称"
            }
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

## Anthropic Claude

### 基础调用

```bash
# 调用 Claude 3 Opus
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $CLAUDE_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"claude-3-opus-20240229\",
    \"prompt\": \"用中文解释什么是区块链\",
    \"max_tokens_to_sample\": 2000,
    \"temperature\": 0.7
  }'
```

"
```

## Google Gemini

### Gemini Pro

```bash
# 调用 Gemini Pro
bash command:"

```sh
curl -X POST \"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GEMINI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"contents\": [{
      \"parts\": [{\"text\": \"用 Python 写一个 hello world\"}]
    }]
  }'
```

"

# Gemini Pro Vision（图片理解）
bash command:"

```sh
curl -X POST \"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=$GEMINI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"contents\": [{
      \"parts\": [
        {\"text\": \"描述这张图片\"},
        {\"inline_data\": {
          \"mime_type\": \"image/jpeg\",
          \"data\": \"$(base64 -w0 image.jpg)\"
        }}
      ]
    }]
  }'
```

"
```

## 多模型对比

```bash
# 批量测试不同模型
write file_path:"~/llm-comparison.sh" content:"

```bash
#!/bin/bash

# 测试问题
QUESTION=\"什么是量子计算？\"

# GPT-4
echo \"=== GPT-4 ===\"
curl -s -X POST https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d \"{\\"model\\": \\"gpt-4\\", \\"messages\\": [{\\"role\\": \\"user\\", \\"content\\": \\"$QUESTION\\"}]}\" | jq '.choices[0].message.content'

# Claude
echo \"=== Claude 3 Opus ===\"
curl -s -X POST https://api.anthropic.com/v1/complete \
  -H \"x-api-key: $CLAUDE_API_KEY\" \
  -H \"anthropic-version: 2023-06-01\" \
  -H \"Content-Type: application/json\" \
  -d \"{\\"model\\": \\"claude-3-opus-20240229\\", \\"prompt\\": \\"Human: $QUESTION\\\\nAssistant:\\", \\"max_tokens_to_sample\": 1000}\" | jq '.completion'

# Gemini
echo \"=== Gemini Pro ===\"
curl -s -X POST \"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GEMINI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d \"{\\"contents\\": [{\\"parts\\": [{\\"text\\": \\"$QUESTION\\"}]}]}\" | jq '.candidates[0].content.parts[0].text'
```

"
```

## 提示词工程

```bash
# 系统提示词模板
SYSTEM_PROMPTS='{
  \"coder\": \"你是一个专业程序员，精通 Python、JavaScript、Go 等语言。代码要有注释，遵循最佳实践。\",
  \"writer\": \"你是一个专业作家，文风清晰流畅，善于解释复杂概念。\",
  \"translator\": \"你是一个专业翻译，精通中英文互译，注意文化差异。\",
  \"analyst\": \"你是一个数据分析师，善于用数据说话，提供有洞察力的分析。\"
}'
```

## 文件位置
`cases/ai-ml/llm-integration.md`
