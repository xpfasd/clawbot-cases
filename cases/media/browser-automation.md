# 浏览器控制案例

## 场景
使用 ClawBot 控制浏览器进行自动化操作

## 基本操作

### 导航

```bash
# 打开网页
browser action:navigate targetUrl:"https://example.com"

# 后台打开
browser action:navigate targetUrl:"https://example.com" target:"background"
```

### 截图

```bash
# 截图当前页面
browser action:screenshot

# 全页面截图
browser action:screenshot fullPage:true
```

### 页面操作

```bash
# 点击元素
browser action:act request:{"kind":"click" selector:"#submit-button"}

# 输入文本
browser action:act request:{"kind":"type" selector:"#email" text:"test@example.com"}

# 滚动页面
browser action:act request:{"kind":"scroll" x:0 y:500}
```

## 自动化场景

### 1. 表单自动填写

```bash
browser action:navigate targetUrl:"https://form.example.com"

# 填写表单
browser action:act request:{"kind":"type" selector:"#name" text:"张三"}
browser action:act request:{"kind":"type" selector:"#email" text:"test@example.com"}
browser action:act request:{"kind":"select" selector:"#country" value:"CN"}

# 提交
browser action:act request:{"kind":"click" selector:"#submit"}
```

### 2. 网页数据采集

```bash
browser action:navigate targetUrl:"https://news.example.com"

# 截图
browser action:screenshot path:"~/news.png"

# 获取页面内容
browser action:snapshot

# 滚动加载更多
browser action:act request:{"kind":"scroll" x:0 y:1000"}
sleep 2
browser action:act request:{"kind":"scroll" x:0 y:2000"}
```

### 3. 登录自动化

```bash
browser action:navigate targetUrl:"https://app.example.com"

# 输入账号
browser action:act request:{"kind":"type" selector:"#username" text:"myaccount"}

# 输入密码
browser action:act request:{"kind":"type" selector:"#password" text:"mypassword"}

# 点击登录
browser action:act request:{"kind":"click" selector:"#login-btn"}

# 等待跳转
sleep 3
```

### 4. 文件上传

```bash
browser action:navigate targetUrl:"https://upload.example.com"

# 点击上传按钮
browser action:act request:{"kind":"click" selector:"#upload-btn"}

# 等待文件选择对话框（需要手动选择）
# 或者使用上传API
browser action:upload filePath:"~/document.pdf"
```

## 高级操作

### 多标签管理

```bash
# 打开新标签
browser action:open targetUrl:"https://example2.com"

# 切换标签
browser action:focus targetId:"tab-2"

# 关闭标签
browser action:close targetId:"tab-2"
```

### iframe 操作

```bash
# 切换到 iframe
browser action:act request:{"kind":"switch" frame:"#iframe-id"}

# 切回主文档
browser action:act request:{"kind":"switch" frame:"parent"}
```

### 等待条件

```bash
# 等待元素出现
browser action:wait selector:"#content" timeoutMs:5000

# 等待页面加载
browser action:wait request:{"kind":"navigation"}
```

## 浏览器配置

```json
{
  "browser": {
    "enabled": true,
    "type": "chromium",
    "headless": false,
    "extensions": [],
    "profile": "default"
  }
}
```

## 注意事项

1. **避免人机验证**：自动化操作可能触发验证码
2. **控制频率**：避免过于频繁的操作
3. **处理弹窗**：注意广告弹窗和确认对话框
4. **隐私安全**：不要在自动化中输入敏感密码

## 文件位置
`cases/media/browser-automation.md`
