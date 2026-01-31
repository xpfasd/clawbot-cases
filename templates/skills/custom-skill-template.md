# 自定义技能模板

## 创建步骤

### 1. 创建技能目录

```
mkdir -p ~/clawbot-cases/skills/my-skill
```

### 2. 创建 SKILL.md

```markdown
---
name: my-skill
description: 我的自定义技能
metadata: {"openclaw":{"emoji":"✨","requires":{"bins":["curl"]}}}
---

# My Skill

这是一个自定义技能示例。

## 使用方法

直接描述你的需求即可。

## 示例

```
用户: 执行我的自定义任务
```
```

### 3. 配置文件

```json
{
  "skills": {
    "entries": {
      "my-skill": {
        "enabled": true
      }
    }
  }
}
```

## 完整模板结构

```
my-skill/
├── SKILL.md          # 技能说明
├── README.md         # 详细文档
├── bin/
│   └── script.sh     # 执行脚本
└── config/
    └── template.json # 配置模板
```

## 元数据字段

| 字段 | 说明 | 必填 |
|------|------|------|
| name | 技能名称 | 是 |
| description | 描述 | 是 |
| metadata.openclaw.emoji | UI emoji | 否 |
| metadata.openclaw.os | 适用系统 | 否 |
| metadata.openclaw.requires.bins | 依赖命令 | 否 |
| metadata.openclaw.requires.env | 环境变量 | 否 |
| metadata.openclaw.requires.config | 配置项 | 否 |

## 文件位置
`templates/skills/custom-skill-template.md`
