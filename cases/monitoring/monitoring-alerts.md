# 监控与告警案例

## 场景
使用 ClawBot 进行系统监控和告警

## 系统监控

### CPU/内存监控

```bash
# 监控系统资源
bash command:"

```sh
# CPU 使用率
top -bn1 | grep \"Cpu(s)\" | awk '{print \"CPU: \" 100-$8 \"%\"}'

# 内存使用
free -h | grep Mem | awk '{print \"内存: \" $3\"/\" $2}'

# 磁盘使用
df -h | grep -E \"^/dev/\" | awk '{print $1 \": \" $5 \"使用\"}'
```

"

# 持续监控
bash command:"

```bash
#!/bin/bash
while true; do
    cpu=$(top -bn1 | grep \"Cpu(s)\" | awk '{print 100-$8}')
    mem=$(free | grep Mem | awk '{print $3/$2 * 100}')
    echo \"$(date): CPU: $cpu%, MEM: $mem%\"
    sleep 60
done
```

"
```

### 服务状态监控

```bash
# 检查服务状态
bash command:"

```bash
#!/bin/bash
services=("nginx" "mysql" "redis" "docker")

for service in \"${services[@]}\"; do
    if systemctl is-active --quiet \"$service\"; then
        echo \"$service: 运行中\"
    else
        echo \"$service: 已停止\"
    fi
done
```

"
```

### 网络监控

```bash
# 网络连通性
bash command:"

```sh
# Ping 测试
ping -c 1 google.com > /dev/null && echo \"网络: 在线\" || echo \"网络: 离线\"

# 端口检测
nc -zv localhost 8080 2>&1 && echo \"8080 端口: 开放\" || echo \"8080 端口: 关闭\"

# 带宽测试
speedtest-cli --simple 2>/dev/null || echo \"无法测试带宽\"
```

"
```

## 应用监控

### 健康检查

```bash
# HTTP 健康检查
bash command:"

```bash
#!/bin/bash
URL=\"$1\"
EXPECTED_STATUS=200

status=$(curl -s -o /dev/null -w \"%{http_code}\" \"$URL\")

if [ \"$status\" = \"$EXPECTED_STATUS\" ]; then
    echo \"健康检查: 通过 (HTTP $status)\"
    exit 0
else
    echo \"健康检查: 失败 (HTTP $status)\"
    exit 1
fi
```

"
```

### 日志监控

```bash
# 错误日志监控
bash command:"

```bash
#!/bin/bash
LOG_FILE=\"$1\"
ERROR_PATTERN=\"ERROR|WARNING|Exception\"

tail -n 0 -f \"$LOG_FILE\" | grep --line-buffered \"$ERROR_PATTERN\" | while read line; do
    echo \"[$(date)] $line\"
    # 可以添加通知逻辑
done
```

"
```

## 告警通知

### 邮件告警

```bash
# 发送告警邮件
bash command:"

```bash
#!/bin/bash
SUBJECT=\"$1\"
BODY=\"$2\"
TO=\"admin@example.com\"

echo \"$BODY\" | mail -s \"$SUBJECT\" \"$TO\"
```

"
```

### Slack 告警

```bash
# 发送 Slack 消息
bash command:"

```bash
#!/bin/bash
WEBHOOK_URL=\"$SLACK_WEBHOOK\"
MESSAGE=\"$1\"

curl -X POST -H 'Content-type: application/json' \
  --data \"{\\\"text\\\": \\\"$MESSAGE\\\"}\" \
  \"$WEBHOOK_URL\"
```

"
```

### 飞书告警

```bash
# 发送飞书消息
bash command:"

```bash
#!/bin/bash
WEBHOOK_URL=\"$FEISHU_WEBHOOK\"
MESSAGE=\"$1\"

curl -X POST \"$WEBHOOK_URL\" \
  -H \"Content-Type: application/json\" \
  -d \"{\\\"msg_type\\\": \\\"text\\\", \\\"content\\\": {\\\"text\\\": \\\"$MESSAGE\\\"}}\"
```

"
```

## 监控告警模板

```json
{
  "name": "system-monitor",
  "description": "系统监控告警模板",
  "version": "1.0.0",
  "type": "monitoring",
  "checks": [
    {
      "name": "cpu-usage",
      "command": "top -bn1 | grep 'Cpu(s)' | awk '{print 100-$8}'",
      "threshold": 80,
      "unit": "%",
      "alert": {
        "level": "warning",
        "message": "CPU 使用率过高"
      }
    },
    {
      "name": "memory-usage",
      "command": "free | grep Mem | awk '{print $3/$2 * 100}'",
      "threshold": 85,
      "unit": "%",
      "alert": {
        "level": "critical",
        "message": "内存使用率过高"
      }
    },
    {
      "name": "disk-usage",
      "command": "df / | tail -1 | awk '{print $5}' | tr -d '%'",
      "threshold": 90,
      "unit": "%",
      "alert": {
        "level": "critical",
        "message": "磁盘空间不足"
      }
    }
  ],
  "notifications": {
    "slack": {
      "enabled": true,
      "webhook_url": "${SLACK_WEBHOOK}"
    },
    "feishu": {
      "enabled": true,
      "webhook_url": "${FEISHU_WEBHOOK}"
    }
  },
  "schedule": {
    "interval": 60,
    "unit": "seconds"
  }
}
```

## Prometheus 集成

```bash
# 查询 Prometheus
bash command:"

```sh
# CPU 使用率
curl \"http://localhost:9090/api/v1/query?query=100-(avg by(instance) (rate(node_cpu_seconds_total{mode='idle'}[5m]))*100)\"

# 内存使用率
curl \"http://localhost:9090/api/v1/query?query=(1-(node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes))*100\"

# 请求率
curl \"http://localhost:9090/api/v1/query?query=rate(http_requests_total[5m])\"
```

"
```

## Grafana 仪表板

```json
{
  "dashboard": {
    "title": "系统监控",
    "panels": [
      {
        "title": "CPU 使用率",
        "type": "graph",
        "targets": [
          {
            "expr": "100 - (avg by(instance) (rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)",
            "legendFormat": "{{instance}}"
          }
        ]
      },
      {
        "title": "内存使用率",
        "type": "graph",
        "targets": [
          {
            "expr": "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100",
            "legendFormat": "{{instance}}"
          }
        ]
      },
      {
        "title": "请求速率",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{status}}"
          }
        ]
      }
    ]
  }
}
```

## 文件位置
`cases/monitoring/monitoring-alerts.md`
