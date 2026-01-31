# 图像生成 AI 案例

## 场景
使用 ClawBot 调用各种图像生成 AI 服务

## DALL-E 3

### 基础生成

```bash
# 生成图像
bash command:"

```sh
curl -X POST https://api.openai.com/v1/images/generations \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -d '{
    \"model\": \"dall-e-3\",
    \"prompt\": \"一只橙色的小猫坐在窗台上看雨，动漫风格，柔和的光线\",
    \"size\": \"1024x1024\",
    \"quality\": \"standard\",
    \"n\": 1
  }'
```

"
```

### 生成变体

```bash
# 基于已有图像生成变体
bash command:"

```sh
curl -X POST https://api.openai.com/v1/images/variations \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"image=@image.png\" \
  -F \"n=4\" \
  -F \"size=\"1024x1024\"\"
```

"
```

## Midjourney

### API 调用（第三方）

```bash
# 使用第三方 Midjourney API
bash command:"

```sh
curl -X POST \"https://api.midjourneyapi.com/imagine\" \
  -H \"Authorization: Bearer $MIDJOURNEY_API_KEY\" \
  -d '{
    \"prompt\": \"cyberpunk city, neon lights, futuristic\",
    \"aspect_ratio\": \"1:1\",
    \"stylize\": 100
  }'
```

"
```

## Stable Diffusion

### 本地部署

```bash
# 使用 Stable Diffusion WebUI API
bash command:"

```sh
# 启动 API
cd stable-diffusion-webui
python launch.py --api

# 生成图像
curl -X POST \"http://127.0.0.1:7860/sdapi/v1/txt2img\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"prompt\": \"a beautiful sunset over the ocean\",
    \"steps\": 20,
    \"width\": 512,
    \"height\": 512,
    \"cfg_scale\": 7
  }'
```

"
```

### ControlNet

```bash
# 使用 ControlNet 控制生成
bash command:"

```sh
curl -X POST \"http://127.0.0.1:7860/sdapi/v1/controlnet/txt2img\" \
  -H \"Content-Type: application/json\" \
  -d '{
    \"prompt\": \"a person walking on the street\",
    \"controlnet_image\": \"base64_encoded_image\",
    \"controlnet_module\": \"openpose\",
    \"steps\": 20
  }'
```

"
```

## 图像编辑

### 局部重绘

```bash
# DALL-E 3 局部编辑
bash command:"

```sh
curl -X POST https://api.openai.com/v1/images/edits \
  -H \"Authorization: Bearer $OPENAI_API_KEY\" \
  -F \"image=@original.png\" \
  -F \"mask=@mask.png\" \
  -F \"prompt=Add a hat to the person\" \
  -F \"n=2\" \
  -F \"size=\"1024x1024\"\"
```

"
```

## 批量生成

```bash
# 批量生成产品图
write file_path:"~/batch-image-gen.sh" content:"

```bash
#!/bin/bash

PRODUCTS=(\"手机\" \"耳机\" \"手表\" \"音箱\")

for product in \"${PRODUCTS[@]}\"; do
    prompt=\"$product on a white background, professional product photography, 4k\"
    
    curl -X POST https://api.openai.com/v1/images/generations \
        -H \"Content-Type: application/json\" \
        -H \"Authorization: Bearer $OPENAI_API_KEY\" \
        -d \"{\\"model\\": \\"dall-e-3\\", \\"prompt\\": \\"$prompt\\", \\"size\\": \\"1024x1024\\", \\"n\\": 1}\" | \
        jq -r '.data[0].url' > \"images/${product}.png\"
    
    echo \"Generated: $product.png\"
done
```

"
```

## 图像处理

### 使用 PIL 处理

```python
from PIL import Image
import requests
from io import BytesIO

# 下载并处理图像
def process_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # 调整大小
    img = img.resize((800, 800))
    
    # 转换为 RGB
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # 保存
    img.save('processed.jpg', 'JPEG', quality=95)
    return img
```

## 文件位置
`cases/ai-ml/image-generation.md`
