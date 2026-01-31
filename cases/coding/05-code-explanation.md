# 代码解释案例

## 场景
使用 ClawBot 解释复杂代码逻辑

## 对话示例

```
用户: 解释这段代码的作用
（粘贴代码）

ClawBot: 代码分析：
1. 函数功能
2. 关键逻辑
3. 复杂度分析
```

## 代码解释示例

### 示例1：递归算法

**代码：**
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

**解释：**
```
这是一个计算斐波那契数列的函数，使用了记忆化递归优化。

关键点：
1. 基础情况：n <= 1 时直接返回 n
2. 递归情况：f(n) = f(n-1) + f(n-2)
3. 优化：使用 memo 字典缓存已计算的结果
   - 避免重复计算
   - 时间复杂度从 O(2^n) 优化到 O(n)

使用场景：
- 需要频繁计算斐波那契数时
- 对性能有要求的递归场景
```

### 示例2：复杂正则

**代码：**
```python
import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

**解释：**
```
电子邮件验证正则表达式分解：

^                        # 字符串开始
[a-zA-Z0-9._%+-]+        # 用户名：字母、数字、._%+-
@                        # @ 符号
[a-zA-Z0-9.-]+           # 域名：字母、数字、.-
\.                       # 点号
[a-zA-Z]{2,}             # 顶级域名：至少2个字母
$                        # 字符串结束

局限性：
- 不支持中文域名
- 不支持特殊字符邮箱
- 不验证邮箱是否真实存在
```

### 示例3：设计模式

**代码：**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**解释：**
```
这是单例模式的 Python 实现。

实现原理：
1. __new__ 方法在 __init__ 之前调用
2. 首次创建时，_instance 为 None，创建实例
3. 后续调用返回已创建的实例

使用场景：
- 数据库连接
- 配置管理器
- 日志记录器
- 全局状态管理

注意事项：
- 多线程环境需要加锁
- 可能会增加耦合度
```

## 代码复杂度分析

| 指标 | 说明 |
|------|------|
| **Cyclomatic Complexity** | 圈复杂度，路径数量 |
| **Cognitive Complexity** | 认知复杂度 |
| **Lines of Code** | 代码行数 |
| **Maintainability Index** | 可维护性指数 |

## 文件位置
`cases/coding/05-code-explanation.md`
