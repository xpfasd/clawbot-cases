# 安全操作案例

## 场景
使用 ClawBot 进行安全相关操作

## 密码管理

### 生成强密码

```bash
# 使用 openssl 生成
bash command:"

```sh
openssl rand -base64 32
```

"

# 使用 pwgen
bash command:"

```sh
pwgen -s 16 1
```

"
```

### 加密文件

```bash
# 使用 GPG 加密
bash command:"

```sh
gpg --symmetric --cipher-algo AES256 secret.txt
# 生成 secret.txt.gpg
```

"

# 解密
bash command:"

```sh
gpg --decrypt secret.txt.gpg
```

"
```

## SSH 密钥管理

### 生成密钥

```bash
# 生成 SSH 密钥
bash command:"

```sh
ssh-keygen -t ed25519 -C \"your_email@example.com\" -f ~/.ssh/id_ed25519
```

"

# 添加到 SSH Agent
bash command:"

```sh
eval \"$(ssh-agent -s)\"
ssh-add ~/.ssh/id_ed25519
```

"
```

### 安全连接

```bash
# SSH 连接到服务器
bash command:"

```sh
ssh -i ~/.ssh/id_ed25519 user@server.com
```

"

# 使用 SSH Config
write file_path:"~/.ssh/config" content:"

```
Host server
    HostName server.com
    User admin
    IdentityFile ~/.ssh/id_ed25519
    AddKeysToAgent yes
```

"
```

## 安全扫描

### 代码安全扫描

```bash
# 使用 npm audit
bash command:"

```sh
cd /path/to/project
npm audit
```

"

# 使用 Trivy 扫描镜像
bash command:"

```sh
trivy image myapp:latest
```

"

# 使用 SonarQube
bash command:"

```sh
sonar-scanner -Dsonar.projectKey=myproject
```

"
```

### 依赖检查

```bash
# Python 安全检查
bash command:"

```sh
pip install safety
safety check
```

"

# Go 安全检查
bash command:"

```sh
go get -u github.com/securego/gosec/cmd/gosec@latest
gosec ./...
```

"
```

## 证书管理

### 生成自签名证书

```bash
# 生成私钥
bash command:"

```sh
openssl genrsa -out server.key 2048
```

"

# 生成证书
bash command:"

```sh
openssl req -new -x509 -key server.key -out server.crt -days 365
```

"
```

## 安全最佳实践

| 操作 | 建议 |
|------|------|
| **密码** | 使用密码管理器，长度 > 16 |
| **SSH** | 使用 ed25519，禁用密码登录 |
| **API Keys** | 存放在环境变量，不提交到 Git |
| **依赖** | 定期更新，扫描漏洞 |
| **证书** | 使用 Let's Encrypt，定期续期 |

## 安全配置示例

```bash
# SSH 强化配置
write file_path:"/etc/ssh/sshd_config.d/hardening.conf" content:"

```
# 禁用 Root 登录
PermitRootLogin no

# 禁用密码登录
PasswordAuthentication no

# 限制登录尝试次数
MaxAuthTries 3

# 设置空闲超时
ClientAliveInterval 300
ClientAliveCountMax 2

# 白名单
AllowUsers admin deploy
```

"
```

## 文件位置
`cases/security/security-operations.md`
