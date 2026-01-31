# 代码重构案例

## 场景
使用 ClawBot 重构和优化现有代码

## 对话示例

```
用户: 重构这段代码，提高可读性和性能
（粘贴代码）

ClawBot: 重构后的代码：
（优化后的代码）
```

## 重构前 vs 重构后

### 案例1：嵌套回调优化

**重构前：**
```javascript
function getUserData(userId, callback) {
    getUser(userId, function(err, user) {
        if (err) {
            callback(err);
            return;
        }
        getOrders(userId, function(err, orders) {
            if (err) {
                callback(err);
                return;
            }
            callback(null, { user, orders });
        });
    });
}
```

**重构后：**
```javascript
async function getUserData(userId) {
    const user = await getUser(userId);
    const orders = await getOrders(userId);
    return { user, orders };
}
```

### 案例2：长函数拆分

**重构前：**
```python
def process_data(data):
    # 数据验证
    if not data:
        return None
    # 数据清洗
    cleaned = []
    for item in data:
        if item['value'] > 0:
            cleaned.append(item)
    # 数据转换
    transformed = []
    for item in cleaned:
        transformed.append({
            'name': item['name'].upper(),
            'value': item['value'] * 2
        })
    # 数据汇总
    total = sum(item['value'] for item in transformed)
    return {'items': transformed, 'total': total}
```

**重构后：**
```python
def process_data(data):
    cleaned = clean_data(data)
    transformed = transform_data(cleaned)
    return summarize_data(transformed)

def clean_data(data):
    return [item for item in data if item['value'] > 0]

def transform_data(cleaned):
    return [{'name': item['name'].upper(), 'value': item['value'] * 2}
            for item in cleaned]

def summarize_data(transformed):
    return {'items': transformed, 'total': sum(item['value'] for item in transformed)}
```

## 重构检查清单

- [ ] 代码清晰易读
- [ ] 函数单一职责
- [ ] 变量命名有意义
- [ ] 减少重复代码
- [ ] 添加必要注释
- [ ] 考虑性能优化

## 文件位置
`cases/coding/02-code-refactoring.md`
