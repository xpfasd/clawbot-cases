# 单元测试案例

## 场景
使用 ClawBot 为代码编写单元测试

## 对话示例

```
用户: 为这个函数编写单元测试
（粘贴代码）

ClawBot: 已生成测试用例：
（测试代码）
```

## 测试框架示例

### Python - pytest

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

class TestCalculator:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
    
    def test_add_mixed_numbers(self):
        assert add(-1, 1) == 0
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0
    
    def test_divide(self):
        assert divide(10, 2) == 5
        with pytest.raises(ValueError):
            divide(10, 0)  # 测试除以零
```

### JavaScript - Jest

```javascript
// calculator.test.js
const { add, subtract, multiply, divide } = require('./calculator');

describe('Calculator', () => {
    describe('add', () => {
        test('adds two positive numbers', () => {
            expect(add(2, 3)).toBe(5);
        });
        
        test('adds two negative numbers', () => {
            expect(add(-1, -1)).toBe(-2);
        });
        
        test('adds mixed numbers', () => {
            expect(add(-1, 1)).toBe(0);
        });
    });
    
    describe('subtract', () => {
        test('subtracts numbers', () => {
            expect(subtract(5, 3)).toBe(2);
        });
    });
    
    describe('divide', () => {
        test('divides numbers', () => {
            expect(divide(10, 2)).toBe(5);
        });
        
        test('throws on division by zero', () => {
            expect(() => divide(10, 0)).toThrow('Division by zero');
        });
    });
});
```

## 测试最佳实践

1. **测试用例覆盖**
   - 正常情况
   - 边界情况
   - 异常情况
   - 错误输入

2. **测试命名**
   - 描述性强
   - 一目了然

3. **Arrange-Act-Assert**
   ```python
   def test_add_two_numbers(self):
       # Arrange
       a = 2
       b = 3
       
       # Act
       result = add(a, b)
       
       # Assert
       assert result == 5
   ```

4. **Mock 和 Stub**
   - 隔离外部依赖
   - 提高测试速度

## 文件位置
`cases/coding/04-unit-testing.md`
