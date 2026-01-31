# 记忆系统使用案例

## 场景
ClawBot 的记忆功能可以记住重要信息和偏好

## 对话示例

```
用户: 记住我的名字叫张三

ClawBot: 已记住！你的名字是张三。

用户: 我叫什么名字？
ClawBot: 你叫张三。

用户: 记住我的项目 deadline 是周五
ClawBot: 已记录！你的项目 deadline 是周五。
```

## 记忆类型

### 1. 长期记忆 (MEMORY.md)
- 用户偏好和设置
- 重要决策和结论
- 长期项目上下文

### 2. 每日记录 (memory/YYYY-MM-DD.md)
- 日常对话摘要
- 工作进度跟踪
- 临时笔记

### 3. 用户信息 (USER.md)
- 用户名称和称呼
- 时区和偏好
- 项目背景

## 手动管理记忆

```bash
# 搜索记忆
openclaw memory search "项目"

# 查看今日记录
openclaw memory today
```

## 自动记忆

AI 会自动记住：
- ✅ 用户明确要求记住的信息
- ✅ 重要决策和结论
- ✅ 项目进度和任务
- ✅ 偏好设置

## 清除记忆

```bash
# 发送 /new 命令开启新对话
/new

# 重置特定记忆（手动编辑文件）
openclaw memory edit
```

## 使用建议

1. **明确记忆**：说"记住..."让 AI 记录重要信息
2. **定期回顾**：让 AI 总结记住的内容
3. **清理不需要的记忆**：保持记忆清晰

## 文件位置
`cases/automation/memory-system.md`
