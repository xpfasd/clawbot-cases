# 日志分析案例

## 场景
使用 ClawBot 分析系统日志

## 日志收集

### 系统日志

```bash
# 查看系统日志
tail -f /var/log/system.log

# 查看应用日志
tail -f /var/log/nginx/access.log

# 查看 Docker 日志
docker logs -f container_name
```

### 搜索日志

```bash
# 搜索错误日志
grep -i error /var/log/syslog

# 搜索特定时间范围
awk '$4 >= "10:00:00" && $4 <= "12:00:00"' /var/log/nginx/access.log

# 统计 404 错误
grep " 404 " /var/log/nginx/access.log | wc -l
```

## 日志分析脚本

### Nginx 日志分析

```bash
# 分析 Nginx 访问日志
write file_path:"~/analyze-nginx.sh" content:"

```bash
#!/bin/bash
LOG_FILE=\"${1:-/var/log/nginx/access.log}\"

echo \"=== Nginx 日志分析 ===\"
echo \"\"

# 访问量统计
echo \"访问量: $(wc -l < $LOG_FILE) 请求\"
echo \"独立 IP: $(awk '{print $1}' $LOG_FILE | sort -u | wc -l)\"
echo \"\"

# 状态码统计
echo \"=== 状态码统计 ===\"
awk '{print $9}' $LOG_FILE | sort | uniq -c | sort -rn
echo \"\"

# 热门页面
echo \"=== Top 10 页面 ===\"
awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -rn | head -10
echo \"\"

# 热门来源
echo \"=== Top 10 来源 IP ===\"
awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -rn | head -10
echo \"\"

# 爬虫统计
echo \"=== 爬虫访问 ===\"
grep -i "bot\|spider\|crawler" $LOG_FILE | awk '{print $1}' | sort | uniq -c | sort -rn | head -5
```

"
```

### 错误日志聚合

```bash
# 聚合错误
write file_path:"~/aggregate-errors.sh" content:"

```bash
#!/bin/bash
LOG_DIR=\"/var/log\"

echo \"=== 系统错误汇总 ===\"
echo \"生成时间: $(date)\"
echo \"\"

# 查找所有错误日志
find $LOG_DIR -name \"*.log\" -exec grep -l \"ERROR\\|Exception\\|Failed\" {} \; | while read logfile; do
    echo \"\"
    echo \"=== $(basename $logfile) ===\"
    tail -100 $logfile | grep -i \"ERROR\\|Exception\\|Failed\" | tail -20
done
```

"
```

## ELK Stack 集成

### 发送到 Elasticsearch

```bash
# 使用 filebeat 收集日志
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/*.log
  fields:
    app: nginx
    env: production

output.elasticsearch:
  hosts: [\"localhost:9200\"]
  index: \"nginx-logs-%{[fields.env]}-%{+yyyy.MM.dd}\"
```

### 查询 Elasticsearch

```bash
# 搜索错误日志
curl -X GET "localhost:9200/nginx-logs-production-2026.01.30/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "match": {
        "status": "500"
      }
    },
    "size": 10
  }'

# 统计状态码分布
curl -X GET "localhost:9200/nginx-logs-production-2026.01.30/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 0,
    "aggs": {
      "status_codes": {
        "terms": {
          "field": "status"
        }
      }
    }
  }'
```

## 文件位置
`cases/analytics/log-analysis.md`
