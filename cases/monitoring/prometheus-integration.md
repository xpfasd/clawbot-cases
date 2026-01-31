# Prometheus 集成案例

## 场景
使用 ClawBot 集成 Prometheus 监控系统

## 安装配置

```bash
# 安装 Prometheus
brew install prometheus

# 或使用 Docker
docker run -d \
  -p 9090:9090 \
  -v prometheus.yml:/etc/prometheus/prometheus.yml \
  --name prometheus \
  prom/prometheus
```

## Prometheus 配置

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: []

rule_files:
  - "alerts.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
  
  - job_name: 'myapp'
    static_configs:
      - targets: ['localhost:8080']
```

## 查询指标

```bash
# 查询 CPU 使用率
curl "http://localhost:9090/api/v1/query?query=100-(avg by(instance) (rate(node_cpu_seconds_total{mode='idle'}[5m]))*100)"

# 查询内存使用率
curl "http://localhost:9090/api/v1/query?query=(1-(node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes))*100"

# 查询请求率
curl "http://localhost:9090/api/v1/query?query=rate(http_requests_total[5m])"

# 查询延迟
curl "http://localhost:9090/api/v1/query?query=histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))"
```

## 告警规则

```yaml
# alerts.yml
groups:
  - name: node_alerts
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "CPU 使用率过高"
          description: "服务器 {{ $labels.instance }} CPU 使用率: {{ $value }}%"
      
      - alert: HighMemoryUsage
        expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 85
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "内存使用率过高"
          description: "服务器 {{ $labels.instance }} 内存使用率: {{ $value }}%"
      
      - alert: DiskSpaceLow
        expr: (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100 > 90
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "磁盘空间不足"
          description: "挂载点 {{ $labels.mountpoint }} 空间使用率: {{ $value }}%"
```

## Grafana 集成

```bash
# 启动 Grafana
docker run -d \
  -p 3000:3000 \
  --name grafana \
  -v grafana-storage:/var/lib/grafana \
  grafana/grafana
```

### Grafana 数据源配置

```json
{
  "name": "Prometheus",
  "type": "prometheus",
  "url": "http://localhost:9090",
  "access": "proxy",
  "isDefault": true
}
```

### Grafana 仪表板

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
        ],
        "alert": {
          "name": "CPU Alert",
          "conditions": [
            {
              "evaluator": {"params": [80], "type": "gt"},
              "operator": {"type": "and"},
              "query": {"params": ["A", "5m", "now"]},
              "reducer": {"type": "avg"},
              "type": "query"
            }
          ],
          "executionErrorState": "alerting",
          "frequency": "60s",
          "handler": 1,
          "message": "CPU 使用率超过 80%",
          "name": "CPU High Alert",
          "noDataState": "no_data",
          "notifications": []
        }
      }
    ]
  }
}
```

## 文件位置
`cases/monitoring/prometheus-integration.md`
