# 密码管理案例

## 场景
使用 ClawBot 安全管理密码和密钥

## 1Password

### 配置

```bash
# 安装 1Password CLI
brew install 1password-cli

# 登录
op signin my.1password.com user@email.com

# 验证
op account get
```

### 获取密码

```bash
# 获取密码
PASSWORD=$(op item get "GitHub" --field "password")

# 获取 API Key
API_KEY=$(op item get "OpenAI" --field "api-key")
```

### 存储密码

```bash
# 创建新项目
op item create \
  --category Login \
  --title "My App" \
  --username "admin" \
  --password "$(openssl rand -base64 32)" \
  --url "https://myapp.com"
```

## HashiCorp Vault

### 启动 Vault

```bash
# 使用 Docker 启动
docker run -d \
  -p 8200:8200 \
  -e VAULT_ADDR=http://localhost:8200 \
  -e VAULT_DEV_ROOT_TOKEN_ID=root \
  --name vault \
  vault

# 导出地址
export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=root
```

### 密钥操作

```bash
# 启用密钥引擎
vault secrets enable -path=secret kv

# 存储密钥
vault kv put secret/myapp/database \
  username=admin \
  password="$(openssl rand -base64 32)"

# 读取密钥
vault kv get secret/myapp/database

# 删除密钥
vault kv delete secret/myapp/database
```

### 动态密钥

```bash
# 启用 AWS 密钥引擎
vault secrets enable -path=aws aws

# 配置 AWS 凭证
vault write aws/config/root \
  access_key=xxx \
  secret_key=yyy \
  region=us-east-1

# 生成动态密钥
vault write aws/roles/my-role \
  credential_type=iam_user \
  policy_arns=arn:aws:iam::aws:policy/ReadOnlyAccess

vault write aws/creds/my-role -format=json
```

## 环境变量管理

```bash
# 创建 .env 文件
write file_path:"~/project/.env.example" content:"

```bash
# API Keys
OPENAI_API_KEY=sk-xxx
ANTHROPIC_API_KEY=sk-ant-xxx
GEMINI_API_KEY=xxx

# Database
DB_PASSWORD=xxx
REDIS_PASSWORD=xxx

# AWS
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx

# 提示：复制此文件为 .env 并填入真实值
```

"

# 使用 .env
source .env
```

## SSH 密钥管理

```bash
# 生成密钥
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519

# 添加到 SSH Agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 上传公钥到服务器
ssh-copy-id user@server.com
```

## 文件位置
`cases/security/password-management.md`
