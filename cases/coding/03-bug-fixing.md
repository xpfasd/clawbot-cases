# Bug 修复案例

## 场景
使用 ClawBot 识别和修复代码中的 Bug

## 对话示例

```
用户: 这段代码有bug，帮我找出来
（粘贴代码）

ClawBot: 发现以下问题：
1. 数组越界
2. 空指针异常
...
修复后的代码：
（修复后的代码）
```

## 常见 Bug 类型

### 1. 数组越界

**Bug 代码：**
```python
def get_last_item(items):
    return items[len(items)]  # ❌ 越界，应该是 len(items)-1
```

**修复后：**
```python
def get_last_item(items):
    return items[-1]  # ✅ 使用负索引
```

### 2. 空指针异常

**Bug 代码：**
```javascript
function getUserName(user) {
    return user.profile.name;  // ❌ user 或 profile 可能为 null
}
```

**修复后：**
```javascript
function getUserName(user) {
    return user?.profile?.name ?? 'Unknown';  // ✅ 可选链 + 空值合并
}
```

### 3. 资源泄漏

**Bug 代码：**
```python
def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    # ❌ 没有关闭文件
    return data
```

**修复后：**
```python
def read_file(filename):
    with open(filename, 'r') as f:  # ✅ 使用 with 语句自动关闭
        return f.read()
```

### 4. 竞态条件

**Bug 代码：**
```javascript
let counter = 0;
function increment() {
    // ❌ 非原子操作
    let temp = counter;
    temp = temp + 1;
    counter = temp;
}
```

**修复后：**
```javascript
let counter = 0;
function increment() {
    // ✅ 使用原子操作
    Atomics.add(counter, 0, 1);
}
// 或者使用 Mutex
```

### 5. 异步处理不当

**Bug 代码：**
```javascript
async function fetchData() {
    const data = await fetch('/api/data');
    console.log(data);
    // ❌ 没有错误处理
}
```

**修复后：**
```javascript
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Failed to fetch data:', error);
        throw error;
    }
}
```

## Debug 技巧

1. **添加日志**：让 AI 添加调试日志
2. **单元测试**：让 AI 编写测试用例覆盖边界情况
3. **代码审查**：让 AI 分析潜在问题
4. **静态分析**：使用工具分析代码质量

## 文件位置
`cases/coding/03-bug-fixing.md`
