# Matrix 集成案例

## 场景
使用 ClawBot 集成 Matrix 通信协议

## 配置

```bash
# 安装 matrix-commander
pip install matrix-commander

# 配置认证
export MATRIX_HOMESERVER="https://matrix.org"
export MATRIX_USER="@bot:matrix.org"
export MATRIX_PASSWORD="your_password"
```

## 发送消息

### 发送文本

```bash
# 发送房间消息
python3 << 'EOF'
import matrix_commander

# 初始化
bot = matrix_commander.MatrixCommander()

# 发送消息
bot.send("Hello from ClawBot!")

# 发送到指定房间
bot.send(room_id="!room_id:matrix.org", message="Hello room!")
EOF
```

### 发送富文本

```python
import matrix_commander

bot = matrix_commander.MatrixCommander()

# 发送格式化的消息
bot.send("""**粗体文本**
*斜体文本*
[链接](https://example.com)
""")
```

## 监听消息

```python
import matrix_commander

class MatrixBot:
    def __init__(self):
        self.bot = matrix_commander.MatrixCommander()
    
    def handle_message(self, room, sender, message):
        print(f"[{room}] {sender}: {message}")
        
        # 回复消息
        if "hello" in message.lower():
            self.bot.send(f"Hi {sender}! 👋")
        
        # 处理命令
        if message.startswith("!"):
            self.handle_command(room, message)
    
    def handle_command(self, room, command):
        if command == "!help":
            self.bot.send("可用命令: !help, !ping, !status")
        elif command == "!ping":
            self.bot.send("Pong! 🏓")
        elif command == "!status":
            self.bot.send("Bot 运行正常 ✅")
    
    def start(self):
        self.bot.listen(messages=True, func=self.handle_message)

# 启动机器人
bot = MatrixBot()
bot.start()
```

## 房间管理

```python
import matrix_commander

bot = matrix_commander.MatrixCommander()

# 创建房间
room_id = bot.create_room(
    alias="clawbot-test",
    name="ClawBot 测试房间",
    is_public=False
)

# 加入房间
bot.join_room(room_id)

# 获取房间成员
members = bot.get_room_members(room_id)
print(members)

# 离开房间
bot.leave_room(room_id)
```

## 文件位置
`cases/integration/matrix-integration.md`
