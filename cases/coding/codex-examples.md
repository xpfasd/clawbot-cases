# 使用 Codex 编程案例

## 场景
使用 ClawBot AI 编程助手帮你写代码

## 使用技能
- `coding-agent` - AI 编程助手

## 对话示例

```
用户: 用 Python 写一个快速排序算法

ClawBot: 正在编写代码...
（生成 Python 代码）
```

## 代码示例

### 快速排序

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 测试
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))
# 输出: [1, 1, 2, 3, 6, 8, 10]
```

### 创建文件

```bash
# 在工作目录创建文件
bash pty:true workdir:~/clawbot-cases command:"codex exec '在 cases/coding 目录下创建 quick_sort.py 文件，实现快速排序算法'"
```

## 常用命令

```bash
# 快速对话
codex exec "写一个 Python 函数计算斐波那契数列"

# 在指定目录工作
bash pty:true workdir:~/project command:"codex exec '重构这个项目的错误处理'"

# 后台运行
bash pty:true background:true command:"codex exec '创建一个贪吃蛇游戏'"
```

## 技巧

- **指定语言**：明确告诉 AI 使用什么语言
- **描述需求**：详细说明功能要求
- **代码审查**：让 AI 检查和改进代码
- **添加注释**：要求 AI 添加详细注释

## 文件位置
`cases/coding/codex-examples.md`
