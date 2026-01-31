#!/bin/bash
# ClawBot 案例库自动扩充脚本
# 功能：每半小时随机添加新的模板或案例

CLAWBOT_DIR=~/clawbot-cases
LOG_FILE=$CLAWBOT_DIR/.auto-expand.log

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

# 随机选择要添加的内容类型
random_type() {
    types=("case" "template" "both")
    echo "${types[$((RANDOM % 3))]}"
}

# 添加随机案例
add_random_case() {
    categories=("coding" "automation" "integration" "ai-ml" "cloud" "analytics" "monitoring" "deployment" "security" "trends")
    category="${categories[$((RANDOM % ${#categories[@]}))]}"
    
    # 根据分类创建不同的案例
    case $category in
        "coding")
            cat > $CLAWBOT_DIR/cases/coding/$(date +%Y%m%d%H%M%S)-random.md << 'EOF'
# 随机编程案例

## 场景
自动生成的编程示例

## 代码示例

```python
def example_function():
    """示例函数"""
    return "Hello, ClawBot!"

# 测试
if __name__ == "__main__":
    print(example_function())
```

## 知识点
- 函数定义
- 文档字符串
- 主入口检查

## 相关案例
- [Codex 基础](../01-codex-basics.md)
- [单元测试](../04-unit-testing.md)

---
*自动生成于 $(date)*
EOF
            ;;
        "automation")
            cat > $CLAWBOT_DIR/cases/automation/$(date +%Y%m%d%H%M%S)-automation.md << 'EOF'
# 随机自动化案例

## 场景
自动生成的自动化任务

## 实现

```bash
#!/bin/bash
# 自动化脚本示例

echo "执行自动化任务: $(date)"
# 这里可以添加实际的自动化逻辑
```

## 定时配置

```json
{
  "schedule": "*/30 * * * *",
  "command": "bash script.sh"
}
```

---
*自动生成于 $(date)*
EOF
            ;;
        "ai-ml")
            cat > $CLAWBOT_DIR/cases/ai-ml/$(date +%Y%m%d%H%M%S)-ai-random.md << 'EOF'
# 随机 AI 案例

## 场景
自动生成的 AI 应用示例

## 实现

```python
# AI 应用示例代码
def ai_example():
    """AI 功能示例"""
    return "AI Integration"

# 调用 API
result = ai_example()
print(result)
```

---
*自动生成于 $(date)*
EOF
            ;;
        *)
            cat > $CLAWBOT_DIR/cases/$category/$(date +%Y%m%d%H%M%S)-${category}.md << 'EOF'
# 随机案例

## 场景
自动生成的内容

## 说明
这是一个自动生成的案例文档。

---
*自动生成于 $(date)*
EOF
            ;;
    esac
    
    log "添加了 $category 案例"
}

# 添加随机模板
add_random_template() {
    template_types=("channel" "skill" "workflow" "database" "deployment")
    type="${template_types[$((RANDOM % ${#template_types[@]}))]}"
    
    case $type in
        "channel")
            cat > $CLAWBOT_DIR/templates/channels/$(date +%Y%m%d%H%M%S)-random.json << 'EOF'
{
  "name": "random-channel",
  "description": "自动生成的通道配置模板",
  "version": "1.0.0",
  "config": {
    "enabled": true,
    "apiKey": "${API_KEY}"
  }
}
EOF
            ;;
        "skill")
            cat > $CLAWBOT_DIR/templates/skills/$(date +%Y%m%d%H%M%S)-random.md << 'EOF'
---
name: random-skill
description: 自动生成的技能模板
metadata: {"openclaw":{"emoji":"✨"}}
---

# Random Skill

自动生成的技能文档。

## 使用方法

直接描述你的需求即可。

---
*自动生成于 $(date)*
EOF
            ;;
        "workflow")
            cat > $CLAWBOT_DIR/templates/workflows/$(date +%Y%m%d%H%M%S)-random.json << 'EOF'
{
  "name": "random-workflow",
  "description": "自动生成的工作流模板",
  "version": "1.0.0",
  "type": "automation"
}
EOF
            ;;
        *)
            cat > $CLAWBOT_DIR/templates/${type}/$(date +%Y%m%d%H%M%S)-random.json << 'EOF'
{
  "name": "random-template",
  "description": "自动生成的配置模板",
  "version": "1.0.0"
}
EOF
            ;;
    esac
    
    log "添加了 $type 模板"
}

# 更新索引文件
update_indexes() {
    # 更新案例库索引
    cd $CLAWBOT_DIR/cases
    find . -name "*.md" -type f | wc -l > .case_count
    log "案例库现有 $(cat .case_count) 个案例"
    
    # 更新模板库索引
    cd $CLAWBOT_DIR/templates
    find . -name "*.md" -o -name "*.json" -type f | wc -l > .template_count
    log "模板库现有 $(cat .template_count) 个模板"
}

# 主程序
main() {
    log "开始自动扩充案例库..."
    
    type=$(random_type)
    
    if [ "$type" == "case" ] || [ "$type" == "both" ]; then
        add_random_case
    fi
    
    if [ "$type" == "template" ] || [ "$type" == "both" ]; then
        add_random_template
    fi
    
    update_indexes
    
    log "自动扩充完成！"
}

# 运行
main
