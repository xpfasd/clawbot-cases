# API 集成案例

## 场景
使用 ClawBot 调用第三方 API

## HTTP 请求

### GET 请求

```bash
# 基础 GET
bash command:"

```sh
curl https://api.example.com/data
```

"

# 带参数
bash command:"

```sh
curl "https://api.example.com/search?q=关键词&limit=10"
```

"

# 带 Headers
bash command:"

```sh
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/protected
```

"
```

### POST 请求

```bash
# POST JSON
bash command:"

```sh
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "email": "test@example.com"}'
```

"

# POST 表单
bash command:"

```sh
curl -X POST https://api.example.com/submit \
  -d "name=张三&email=test@example.com"
```

"
```

## 常用 API 示例

### 1. 天气 API

```bash
# OpenWeatherMap
bash command:"

```sh
curl "https://api.openweathermap.org/data/2.5/weather?q=北京&appid=YOUR_API_KEY&units=metric"
```

"
```

### 2. GitHub API

```bash
# 获取用户信息
bash command:"

```sh
curl -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/users/username
```

"

# 创建 Issue
bash command:"

```sh
curl -X POST \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/owner/repo/issues \
  -d '{"title": "Bug 报告", "body": "描述..."```

### 3. 飞}'
```

"
书 API

```bash
# 获取用户信息
bash command:"

```sh
curl -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "APP_ID", "app_secret": "APP_SECRET"}'
```

"
```

## API 封装示例

```bash
# 创建 API 工具脚本
write file_path:"~/api-utils.sh" content:"

```bash
#!/bin/bash

# API 基地址
BASE_URL=\"https://api.example.com\"

# GET 请求
api_get() {
    endpoint=\"$1\"
    curl -s \"${BASE_URL}${endpoint}\"
}

# POST 请求
api_post() {
    endpoint=\"$1\"
    data=\"$2\"
    curl -s -X POST \"${BASE_URL}${endpoint}\" \
        -H \"Content-Type: application/json\" \
        -d \"$data\"
}

# 带认证的请求
api_auth_get() {
    endpoint=\"$1\"
    token=\"$2\"
    curl -s -H \"Authorization: Bearer ${token}\" \"${BASE_URL}${endpoint}\"
}
```

"
```

## 处理 API 响应

```bash
# 解析 JSON
bash command:"

```sh
# 使用 jq 解析
curl -s https://api.example.com/data | jq '.result[0].name'
```

"

# 条件判断
bash command:"

```sh
response=$(curl -s https://api.example.com/status)
status=$(echo \"$response\" | jq -r '.status')

if [ \"$status\" = \"success\" ]; then
    echo \"操作成功\"
else
    echo \"操作失败\"
fi
```

"
```

## 错误处理

```bash
# 检查 HTTP 状态码
bash command:"

```bash
#!/bin/bash
response=$(curl -s -w \"%{http_code}\" https://api.example.com/data)
http_code=$(echo \"$response\" | tail -n1)
body=$(echo \"$response\" | sed '$d')

if [ \"$http_code\" = \"200\" ]; then
    echo \"成功: $body\"
else
    echo \"失败 ($http_code): $body\"
fi
```

"
```

## API 速率限制

```bash
# 检查速率限制
bash command:"

```sh
curl -i https://api.example.com/data 2>&1 | grep -i ratelimit
```

"

# 等待限流恢复
bash command:"

```bash
#!/bin/bash
while true; do
    response=$(curl -s -o /dev/null -w \"%{http_code}\" https://api.example.com/data)
    if [ \"$response\" != \"429\" ]; then
        break
    fi
    echo \"Rate limited, waiting...\"
    sleep 5
done
```

"
```

## 文件位置
`cases/integration/api-integration.md`
