# 数据库操作案例

## 场景
使用 ClawBot 连接和操作数据库

## 支持的数据库

| 数据库 | 驱动/工具 | 难度 |
|--------|-----------|------|
| SQLite | sqlite3 | ⭐ |
| PostgreSQL | psql/pg | ⭐⭐ |
| MySQL | mysql | ⭐⭐ |
| MongoDB | mongosh | ⭐⭐ |
| Redis | redis-cli | ⭐ |

## SQLite 操作

### 连接数据库

```bash
# 创建/连接数据库
bash command:"sqlite3 ~/data.db \"CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);\""

# 查看表结构
bash command:"sqlite3 ~/data.db \".schema users\""
```

### 增删改查

```bash
# 插入数据
bash command:"sqlite3 ~/data.db \"INSERT INTO users (name) VALUES ('张三');\""

# 查询数据
bash command:"sqlite3 ~/data.db \"SELECT * FROM users;\""

# 更新数据
bash command:"sqlite3 ~/data.db \"UPDATE users SET name='李四' WHERE id=1;\""

# 删除数据
bash command:"sqlite3 ~/data.db \"DELETE FROM users WHERE id=1;\""
```

## PostgreSQL 操作

### 连接数据库

```bash
# 连接数据库
bash command:"

```sh
psql -h localhost -U postgres -d mydb
```

"
```

### SQL 操作

```bash
# 创建表
bash command:"

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW()
);
```

"

# 插入
bash command:"

```sql
INSERT INTO tasks (title) VALUES ('完成报告');
```

"

# 查询
bash command:"

```sql
SELECT * FROM tasks WHERE status = 'pending';
```

"
```

## MongoDB 操作

### 连接

```bash
# 连接 MongoDB
bash command:"mongosh \"mongodb://localhost:27017/mydb\""
```

### CRUD 操作

```javascript
// 插入文档
db.users.insertOne({ name: "张三", age: 25 })

// 查询
db.users.find({ age: { $gt: 20 } })

// 更新
db.users.updateOne(
    { name: "张三" },
    { $set: { age: 26 } }
)

// 删除
db.users.deleteOne({ name: "张三" })
```

## Redis 操作

```bash
# 连接
bash command:"redis-cli"

# 基本操作
SET user:name "张三"
GET user:name
INCR counter
DEL key

# 哈希
HSET user name "张三" age 25
HGETALL user
```

## 自动化数据库备份

```bash
# Cron 定时备份 PostgreSQL
openclaw cron add \
  --name "数据库备份" \
  --schedule "0 3 * * *" \
  --payload "执行备份命令"

# 备份脚本
bash command:"

```sh
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U postgres mydb > ~/backups/mydb_$DATE.sql
gzip ~/backups/mydb_$DATE.sql
```

"
```

## 文件位置
`cases/database/database-operations.md`
