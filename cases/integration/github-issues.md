# GitHub Issue 管理案例

## 场景
使用 ClawBot 管理 GitHub Issues

## 使用技能
- `github` - GitHub 操作

## 对话示例

```
用户: 列出我的仓库的所有 open 状态的 issues

ClawBot: 📋 Issues 列表 (open)
#1 - 添加天气功能 (feature)
#2 - 修复登录 bug (bug)
#3 - 更新文档 (docs)
```

## 常用命令

```bash
# 列出 issues
gh issue list --state open

# 创建 issue
gh issue create --title "新功能" --body "描述"

# 查看 issue
gh issue view 1

# 关闭 issue
gh issue close 1
```

## 代码示例

```json
{
  "skill": "github",
  "action": "list_issues",
  "params": {
    "state": "open",
    "limit": 10
  }
}
```

## 文件位置
`cases/integration/github-issues.md`
