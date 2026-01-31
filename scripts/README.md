# ClawBot 案例库自动化扩展系统

> 本项目包含自动化的案例和模板扩展功能

## 🚀 自动扩充系统

### 功能说明

系统每 **30 分钟** 自动执行一次脚本，随机添加：
- ✅ 新的使用案例 (Cases)
- ✅ 新的配置模板 (Templates)
- ✅ 更新索引文件

### 脚本位置

```
scripts/
├── auto-expand.sh          # 自动扩充主脚本
└── README.md               # 本说明文件
```

### 运行日志

日志保存在：`.auto-expand.log`

### 手动触发

```bash
# 手动运行扩充脚本
bash ~/clawbot-cases/scripts/auto-expand.sh

# 查看日志
tail -f ~/clawbot-cases/.auto-expand.log
```

### 定时任务状态

```bash
# 查看定时任务
openclaw cron list

# 查看任务详情
openclaw cron show 29d85396-a634-48b6-a541-fe13e4511681

# 删除定时任务
openclaw cron rm 29d85396-a634-48b6-a541-fe13e4511681
```

## 📊 统计信息

| 指标 | 数量 |
|------|------|
| 案例文档 | 40+ |
| 配置模板 | 45+ |
| 分类目录 | 20+ |
| 运行周期 | 每 30 分钟 |

## 🔧 自定义配置

### 修改运行周期

```bash
# 编辑定时任务
openclaw cron edit 29d85396-a634-48b6-a541-fe13e4511681 \
  --every "1h"  # 改为每小时
```

### 禁用自动扩充

```bash
# 禁用任务
openclaw cron disable 29d85396-a634-48b6-a541-fe13e4511681
```

## 📝 自动化流程

1. **触发**：每 30 分钟自动触发
2. **随机选择**：随机选择要添加的内容类型（案例/模板/两者）
3. **生成内容**：根据分类生成随机案例或模板
4. **更新索引**：更新索引文件统计数量
5. **记录日志**：记录到 .auto-expand.log

## 🎯 支持的分类

### 案例分类
- `coding` - 编程案例
- `automation` - 自动化案例
- `integration` - 集成案例
- `ai-ml` - AI/ML 案例
- `cloud` - 云服务案例
- `analytics` - 数据分析案例
- `monitoring` - 监控案例
- `deployment` - 部署案例
- `security` - 安全案例
- `trends` - 热搜趋势案例

### 模板分类
- `channels` - 消息通道模板
- `skills` - 技能配置模板
- `workflows` - 工作流模板
- `database` - 数据库模板
- `deployment` - 部署模板
- `google-ai` - Google AI 模板
- `ai-tools` - AI 工具模板

## ⚠️ 注意事项

1. 自动生成的内容是基础模板，可能需要手动完善
2. 日志文件会逐渐增大，建议定期清理
3. 如需停止自动扩充，删除定时任务即可

---

*自动化系统由 ClawDBot 🦞 驱动*
