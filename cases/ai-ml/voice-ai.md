# 语音 AI 案例

## 场景
使用 ClawBot 调用语音合成和语音识别服务

## 语音合成 (TTS)

### ElevenLabs

```bash
# 生成语音
bash command:"

```sh
curl -X POST \"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM\" \
  -H \"Accept: audio/mpeg\" \
  -H \"Content-Type: application/json\" \
  -H \"xi-api-key: $ELEVENLABS_API_KEY\" \
  -d '{
    \"text\": \"你好，这是语音合成测试。\",
    \"model_id\": \"eleven_monolingual_v1\",
    \"voice_settings\": {
      \"stability\": 0.5,
      \"similarity_boost\": 0.75
    }
  }' \
  -o output.mp3
```

"
```

### 声音列表

```bash
# 获取可用声音
bash command:"

```sh
curl -X GET \"https://api.elevenlabs.io/v1/voices\" \
  -H \"xi-api-key: $ELEVENLABS_API_KEY\"
```

"
```

### Google TTS

```bash
# 使用 Google Cloud TTS
bash command:"

```sh
gcloud text-to-speech synthesize \
  --input-text=\"你好，世界\" \
  --language-code=\"zh-CN\" \
  --voice=\"zh-CN-Wavenet-A\" \
  --audio-config=\"audioEncoding=MP3\" \
  --output-file=\"output.mp3\"
```

"
```

### OpenAI TTS

```bash
# OpenAI TTS
bash command:"

```sh
curl -X POST https://api.openai.com/v1/audio/speech \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"model\": \"tts-1\",
    \"input\": \"Hello, this is a test of the OpenAI text to speech API.\",
    \"voice\": \"alloy\",
    \"speed\": 1.0
  }' \
  -o speech.mp3
```

"
```

## 语音识别 (STT)

### Whisper 本地

```bash
# 安装 Whisper
pip install openai-whisper

# 转写音频
whisper audio.mp3 --model medium --language Chinese

# 指定格式
whisper audio.mp3 --model medium --output_format srt
```

### Whisper API

```bash
# OpenAI Whisper API
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

### Google Speech-to-Text

```bash
# 配置
export GOOGLE_APPLICATION_CREDENTIALS=\"credentials.json\"

# 转写
gcloud speech recognize-long-audio-config \
  --uri=\"gs://your-bucket/audio.wav\" \
  --language-code=\"zh-CN\" \
  --enable-word-time-offsets \
  audio-file.json
```

## 语音翻译

```bash
# Whisper 翻译（音频 -> 英文文本）
bash command:"

```sh
curl -X POST https://api.openai.com/v1/audio/translations \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"file=@chinese_audio.mp3\" \
  -F \"model=whisper-1\" \
  -F \"response_format=text\"
```

"
```

## 语音活动检测

```bash
# 使用 Silero VAD
pip install silero-vad

python3 << 'EOF'
import torch
import torchaudio
from silero_vad import load_silero_vad, read_audio

vad_model = load_silero_vad()

audio = read_audio('audio.wav')
speech_timestamps = get_speech_timestamps(audio, vad_model, return_seconds=True)

print(f\"检测到 {len(speech_timestamps)} 段语音\")
for ts in speech_timestamps:
    print(f\"  {ts['start']:.2f}s - {ts['end']:.2f}s\")
EOF
```

## 文件位置
`cases/ai-ml/voice-ai.md`
