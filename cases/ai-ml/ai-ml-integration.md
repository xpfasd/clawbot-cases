# AI/ML 集成案例

## 场景
使用 ClawBot 调用 AI/ML 服务

## 文本生成

### OpenAI GPT

```bash
# 调用 GPT API
bash command:"

```sh
curl -X POST https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"gpt-4\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"用 Python 写一个快速排序\"}
    ]
  }'
```

"
```

### Anthropic Claude

```bash
# 调用 Claude API
bash command:"

```sh
curl -X POST https://api.anthropic.com/v1/complete \
  -H \"Content-Type: application/json\" \
  -H \"x-api-key: $CLAUDE_API_KEY\" \
  -d '{
    \"model\": \"claude-3-opus-20240229\",
    \"prompt\": \"用 Python 写一个快速排序\",
    \"max_tokens_to_sample\": 1000
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
    \"prompt\": \"一只在太空中的蓝色龙虾，赛博朋克风格\",
    \"size\": \"1024x1024\"
  }'
```

"
```

### Stable Diffusion

```bash
# 使用 Stability AI
bash command:"

```sh
curl -X POST \"https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image\" \
  -H \"Authorization: Bearer $STABILITY_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"text_prompts\": [{\"text\": \"一只在太空中的蓝色龙虾\"}],
    \"cfg_scale\": 7,
    \"width\": 1024,
    \"height\": 1024
  }'
```

"
```

## 语音合成

### ElevenLabs TTS

```bash
# 生成语音
bash command:"

```sh
curl -X POST \"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM\" \
  -H \"Accept: audio/mpeg\" \
  -H \"Content-Type: application/json\" \
  -H \"xi-api-key: $ELEVENLABS_API_KEY\" \
  -d '{
    \"text\": \"你好，这是一个语音合成测试\",
    \"model_id\": \"eleven_monolingual_v1\"
  }' \
  -o output.mp3
```

"
```

## 语音识别

### Whisper

```bash
# 转写音频
bash command:"

```sh
whisper audio.mp3 --model medium --language Chinese
```

"
```

### OpenAI Whisper API

```bash
# API 转写
bash command:"

```sh
curl -X POST https://api.openai.com/v1/audio/transcriptions \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -H \"Content-Type: multipart/form-data\" \
  -F \"file=@audio.mp3\" \
  -F \"model=whisper-1\" \
  -F \"language=zh\"
```

"
```

## 嵌入向量

### OpenAI Embeddings

```bash
# 生成嵌入
bash command:"

```sh
curl -X POST https://api.openai.com/v1/embeddings \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"text-embedding-3-small\",
    \"input\": [\"你好\", \"世界\"]
  }'
```

"
```

## 向量数据库

### Pinecone 示例

```bash
# 插入向量
bash command:"

```sh
curl -X POST \"https://controller.pinecone.io/databases/YOUR_INDEX/vectors\" \
  -H \"Content-Type: application/json\" \
  -H \"Api-Key: $PINECONE_API_KEY\" \
  -d '{
    \"vectors\": [
      {\"id\": \"vec1\", \"values\": [0.1, 0.2, 0.3], \"metadata\": {\"text\": \"示例文本\"}}
    ]
  }'
```

"

# 查询
bash command:"

```sh
curl -X POST \"https://controller.pinecone.io/databases/YOUR_INDEX/query\" \
  -H \"Content-Type: application/json\" \
  -H \"Api-Key: $PINECONE_API_KEY\" \
  -d '{
    \"vector\": [0.1, 0.2, 0.3],
    \"topK\": 5
  }'
```

"
```

## 批量处理

```bash
# 批量文本处理
bash command:"

```bash
#!/bin/bash
# 处理多个文本

texts=(
    \"文本1\"
    \"文本2\"
    \"文本3\"
)

for text in \"${texts[@]}\"; do
    curl -X POST https://api.openai.com/v1/embeddings \
        -H \"Content-Type: application/json\" \
        -H \"Authorization: Bearer $OPENAI_API_KEY\" \
        -d \"{\\\"model\\\": \\\"text-embedding-3-small\\\", \\\"input\\\": \\\"$text\\\"}\"
done
```

"
```

## 文件位置
`cases/ai-ml/ai-ml-integration.md`
