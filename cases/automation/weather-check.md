# 天气查询案例

## 场景
使用 ClawBot 查询天气

## 使用技能
- `weather` - 天气查询（无需 API Key）

## 对话示例

```
用户: 今天北京天气怎么样？

ClawBot: 🌤️ 北京今日天气
- 温度: 15°C
- 天气: 多云
- 风力: 3级
```

## 代码实现

```json
{
  "skill": "weather",
  "command": "get_forecast",
  "params": {
    "city": "北京",
    "days": 1
  }
}
```

## 扩展用法

- 查询多天预报：`未来一周天气`
- 查询其他城市：`上海天气`
- 带时间：`明天天气`

## 文件位置
`cases/automation/weather-check.md`
