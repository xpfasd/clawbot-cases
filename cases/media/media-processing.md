# 媒体处理案例

## 场景
使用 ClawBot 处理图片、音频、视频等媒体文件

## 图片处理

### 基本操作

```bash
# 图片分析
image image:"~/photo.jpg" prompt:"描述这张图片的内容"

# 图片生成（使用 AI）
bash command:"

```sh
# 使用 DALL-E 或其他工具
openai images generate --prompt \"一只在太空中的龙虾\" --size 1024
```

"
```

### 图片编辑

```bash
# 调整大小
bash command:"

```sh
# 使用 ImageMagick
convert input.jpg -resize 800x600 output.jpg

# 保持比例
convert input.jpg -resize 800x output.jpg
```

"

# 格式转换
bash command:"convert input.png output.jpg"
```

### 截图操作

```bash
# 屏幕截图
nodes action:screen_record node:local outPath:"~/screenshot.png" durationMs:1000

# 相机拍照
nodes action:camera_snap node:local outPath:"~/camera.jpg"
```

## 音频处理

### 语音转文字

```bash
# 使用 OpenAI Whisper
bash command:"

```sh
# 本地转写
whisper audio.mp3 --model medium

# 或使用 API
openai audio transcribe --file audio.mp3
```

"
```

### 文字转语音

```bash
# 使用 ElevenLabs TTS
tts text:"你好，这是语音合成" channel:feishu

# 或使用 sag 工具
bash command:"sag \"Hello World\""
```

### 音频编辑

```bash
# 剪辑音频
bash command:"

```sh
# 使用 ffmpeg
ffmpeg -i input.mp3 -ss 00:01:00 -to 00:02:00 -c copy output.mp3

# 提取音频
ffmpeg -i video.mp4 -vn -acodec copy audio.aac
```

"
```

## 视频处理

### 基本操作

```bash
# 视频截图
bash command:"

```sh
# 提取特定帧
ffmpeg -i video.mp4 -ss 00:01:30 -vframes 1 screenshot.jpg

# 生成缩略图
ffmpeg -i video.mp4 -vf \"fps=1,scale=320:-1\" thumb_%04d.jpg
```

"

# 视频剪辑
bash command:"

```sh
ffmpeg -i input.mp4 -ss 00:00:10 -to 00:01:00 -c copy clip.mp4
```

"
```

### 视频转码

```bash
# 压缩视频
bash command:"

```sh
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 output.mp4

# 转换格式
ffmpeg -i input.avi output.mp4
```

"
```

## 媒体文件上传

### 飞书上传

```bash
# 上传图片
message action:send channel:feishu message:"图片如下" media:"~/photo.jpg"

# 上传文件
message action:send channel:feishu message:"文件如下" filePath:"~/document.pdf"
```

## 最佳实践

| 操作 | 建议 |
|------|------|
| **图片大小** | 压缩到 1MB 以下 |
| **视频时长** | 尽量简短 |
| **格式选择** | 使用通用格式 (jpg, mp4, mp3) |
| **处理工具** | ffmpeg, ImageMagick, whisper |

## 文件位置
`cases/media/media-processing.md`
