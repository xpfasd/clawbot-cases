# Cron 定时任务案例

## 场景
使用 ClawBot 设置定时提醒和自动化任务

## 对话示例

```
用户: 每天早上9点提醒我写日报

ClawBot: 已设置！每天早上 9:00 提醒你写日报。
```

## 命令行操作

```bash
# 添加定时任务
openclaw cron add \
  --name "每日提醒" \
  --schedule "0 9 * * *" \
  --payload "提醒: 该写日报了！"

# 列出所有任务
openclaw cron list

# 运行任务
openclaw cron run <jobId>

# 查看任务历史
openclaw cron runs <jobId>

# 删除任务
openclaw cron remove <jobId>
```

## Cron 表达式格式

| 表达式 | 含义 |
|--------|------|
| `* * * * *` | 每分钟 |
| `0 * * * *` | 每小时 |
| `0 9 * * *` | 每天早上9点 |
| `0 9 * * 1` | 每周一早上9点 |
| `0 9 1 * *` | 每月1号早上9点 |
| `0 9 * * 1-5` | 工作日早上9点 |

## 实用案例

### 案例1：每日天气提醒

```bash
openclaw cron add \
  --name "天气提醒" \
  --schedule "0 7 * * *" \
  --payload "查询今天天气并提醒用户"
```

### 案例2：每周项目回顾

```bash
openclaw cron add \
  --name "周项目回顾" \
  --schedule "0 18 * * 5" \
  --payload "提醒进行每周项目回顾"
```

### 案例3：定时备份

```bash
openclaw cron add \
  --name "数据备份" \
  --schedule "0 3 * * 0" \
  --payload "执行数据备份任务"
```

## 系统事件

可以配置系统事件触发：

```json
{
  "name": "定时任务",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * *",
    "tz": "Asia/Shanghai"
  },
  "payload": {
    "kind": "systemEvent",
    "text": "提醒用户"
  },
  "sessionTarget": "main"
}
```

## 文件位置
`cases/automation/cron-tasks.md`
