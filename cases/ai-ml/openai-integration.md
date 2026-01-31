# ChatGPT/OpenAI 集成案例

## 场景
使用 ClawBot 调用 OpenAI 服务

## API 配置

```bash
# 设置 API Key
export OPENAI_API_KEY="sk-your-api-key"
```

## 文本生成

### GPT-4

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
      {\"role\": \"user\", \"content\": \"用 Python 写一个简单的 Web 服务器\"}
    ],
    \"temperature\": 0.7,
    \"max_tokens\": 2000
  }'
```

"
```

### GPT-3.5 Turbo

```bash
# 调用 GPT-3.5
bash command:"

```sh
curl -X POST https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"gpt-3.5-turbo\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"解释什么是 RESTful API\"}
    ]
  }'
```

"
```

## 图像生成

### DALL-E 3

```bash
# 生成图像
bash command:"

```sh
curl -X POST https://api.openai.com/v1/images/generations \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"dall-e-3\",
    \"prompt\": \"一只橙色的小猫坐在窗台上看雨，动漫风格\",
    \"size\": \"1024x1024\",
    \"quality\": \"standard\",
    \"n\": 1
  }'
```

"
```

### DALL-E 2

```bash
# DALL-E 2 生成
bash command:"

```sh
curl -X POST https://api.openai.com/v1/images/generations \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"dall-e-2\",
    \"prompt\": \"极简风格的办公室设计\",
    \"size\": \"256x256\",
    \"n\": 4
  }'
```

"
```

## 语音识别

### Whisper API

```bash
# 音频转文字
bash command:"

```sh
curl -X POST https://api.openai.com/v1/audio/transcriptions \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"file=@audio.mp3\" \
  -F \"model=whisper-1\" \
  -F \"language=zh\" \
  -F \"response_format=verbose_json\"
```

"
```

### 翻译

```bash
# 音频翻译（自动识别并翻译成英文）
bash command:"

```sh
curl -X POST https://api.openai.com/v1/audio/translations \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"file=@audio.mp3\" \
  -F \"model=whisper-1\"
```

"
```

## 嵌入向量

### Embeddings

```bash
# 生成文本嵌入
bash command:"

```sh
curl -X POST https://api.openai.com/v1/embeddings \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"text-embedding-3-small\",
    \"input\": [\"你好世界\", \"机器学习\", \"人工智能\"]
  }'
```

"
```

## 微调模型

### 上传训练数据

```bash
# 准备训练数据
write file_path:"~/training-data.jsonl" content:"

{\"prompt\": \"中国的首都是？\", \"completion\": \"中国的首都是北京。\"}
{\"prompt\": \"2+2 等于几？\", \"completion\": \"2+2 等于 4。\"}
{\"prompt\": \"太阳是什么颜色的？\", \"completion\": \"太阳看起来是白色的，但通过大气散射后呈现黄色。\"}
```

"

# 上传文件
bash command:"

```sh
curl -X POST https://api.openai.com/v1/files \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"purpose=fine-tune\" \
  -F \"file=@training-data.jsonl\"
```

"
```

## 批量处理

```bash
# 批量文本处理
write file_path:"~/batch-process.sh" content:"

```bash
#!/bin/bash
INPUT_FILE=\"$1\"
OUTPUT_FILE=\"$2\"

while IFS= read -r line; do
    response=$(curl -s -X POST https://api.openai.com/v1/chat/completions \
        -H \"Content-Type: application/json\" \
        -H \"Authorization: Bearer $OPENAI_API_KEY\" \
        -d \"{\\"model\\": \\"gpt-3.5-turbo\\", \\"messages\\": [{\\"role\\": \\"user\\", \\"content\\": \\"$line\\"}]}\")
    
    result=$(echo \"$response\" | jq -r '.choices[0].message.content')
    echo \"$result\" >> \"$OUTPUT_FILE\"
done < \"$INPUT_FILE\"
```

"
```

## 成本统计

```bash
# 计算 API 成本
write file_path:"~/cost-calculator.py" content:"

```python
import json

# 定价 (USD)
PRICING = {
    'gpt-4': {'input': 0.03, 'output': 0.06},
    'gpt-4-32k': {'input': 0.06, 'output': 0.12},
    'gpt-3.5-turbo': {'input': 0.0005, 'output': 0.0015},
    'dall-e-3': {'price': 0.04},  # per image
    'whisper': {'price': 0.006},  # per minute
}

def calculate_cost(model, input_tokens, output_tokens):
    if model not in PRICING:
        return None
    
    if 'input' in PRICING[model]:
        cost = (input_tokens / 1000) * PRICING[model]['input']
        cost += (output_tokens / 1000) * PRICING[model]['output']
    else:
        cost = PRICING[model]['price']
    
    return cost

# 使用示例
cost = calculate_cost('gpt-4', 1000, 2000)
print(f\"预计成本: ${cost:.4f}\")
```

"
```

## 文件位置
`cases/ai-ml/openai-integration.md`
