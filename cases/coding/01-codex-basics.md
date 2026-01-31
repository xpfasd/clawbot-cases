# 编程案例集

> ClawBot 编程相关使用案例

## 📁 目录

1. [Codex 编程助手](#codex-编程助手)
2. [代码重构](#代码重构)
3. [Bug 修复](#bug-修复)
4. [单元测试](#单元测试)
5. [代码解释](#代码解释)

---

## Codex 编程助手

### 基本用法

```markdown
## 场景
使用 ClawBot AI 编程助手帮你写代码

## 对话示例
```
用户: 用 Python 写一个快速排序算法

ClawBot: 正在编写代码...
（生成 Python 代码）
```

## 代码示例

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

## 创建文件

```bash
bash pty:true workdir:~/clawbot-cases command:"codex exec '在 cases/coding 目录下创建 quick_sort.py 文件'"
```

## 技巧
- 明确告诉 AI 使用什么语言
- 详细说明功能要求
- 要求添加详细注释
