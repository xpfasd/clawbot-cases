# 部署案例

## 场景
使用 ClawBot 进行应用部署

## Docker 部署

### 构建镜像

```bash
# 构建 Docker 镜像
bash command:"

```sh
docker build -t myapp:latest .
```

"

# 打标签
bash command:"

```sh
docker tag myapp:latest myregistry.com/myapp:v1.0
```

"

# 推送
bash command:"

```sh
docker push myregistry.com/myapp:v1.0
```

"
```

### 运行容器

```bash
# 运行
bash command:"

```sh
docker run -d -p 8080:80 --name myapp myapp:latest
```

"

# 查看日志
bash command:"

```sh
docker logs -f myapp
```

"

# 停止
bash command:"

```sh
docker stop myapp && docker rm myapp
```

"
```

### Docker Compose

```bash
# 启动服务
bash command:"

```sh
docker-compose up -d
```

"

# 查看状态
bash command:"

```sh
docker-compose ps
```

"

# 查看日志
bash command:"

```sh
docker-compose logs -f
```

"

# 停止
bash command:"

```sh
docker-compose down
```

"
```

## Kubernetes 部署

### 基本操作

```bash
# 应用配置
bash command:"

```sh
kubectl apply -f deployment.yaml
```

"

# 查看 Pods
bash command:"

```sh
kubectl get pods
```

"

# 查看日志
bash command:"

```sh
kubectl logs -f pod/myapp-pod-xxx
```

"

# 扩缩容
bash command:"

```sh
kubectl scale deployment/myapp --replicas=3
```

"

# 更新镜像
bash command:"

```sh
kubectl set image deployment/myapp myapp=myapp:v2.0
```

"
```

### 部署配置示例

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:v1.0
        ports:
        - containerPort: 80
```

## SSH 远程部署

```bash
# 连接到服务器并部署
bash command:"

```sh
#!/bin/bash
ssh user@server.com << 'EOF'
    cd /var/www/myapp
    git pull origin main
    docker-compose up -d --build
    docker system prune -f
EOF
```

"
```

## 自动化部署工作流

```bash
# 完整部署脚本
write file_path:"~/deploy.sh" content:"

```bash
#!/bin/bash
set -e

echo \"开始部署...\"

# 1. 拉取代码
echo \"拉取代码...\"
git pull origin main

# 2. 构建
echo \"构建 Docker 镜像...\"
docker build -t myapp:$VERSION .

# 3. 测试
echo \"运行测试...\"
docker run myapp:$VERSION npm test

# 4. 推送
echo \"推送到仓库...\"
docker tag myapp:$VERSION $REGISTRY/myapp:$VERSION
docker push $REGISTRY/myapp:$VERSION

# 5. 部署
echo \"部署到服务器...\"
ssh $SERVER \"cd /app && docker-compose pull && docker-compose up -d\"

# 6. 验证
echo \"验证部署...\"
curl -f https://myapp.example.com/health

echo \"部署完成!\"
```

"
```

## 部署监控

```bash
# 检查服务状态
bash command:"

```sh
# 检查进程
ps aux | grep myapp

# 检查端口
netstat -tlnp | grep 8080

# 检查资源使用
docker stats
```

"

# 健康检查
bash command:"

```sh
curl -f http://localhost:8080/health || echo \"服务异常\"
```

"
```

## 回滚

```bash
# Docker 回滚
bash command:"

```sh
docker-compose down
docker-compose pull
docker-compose up -d
```

"

# Kubernetes 回滚
bash command:"

```sh
kubectl rollout undo deployment/myapp
```

"
```

## 文件位置
`cases/deployment/docker-deployment.md`
