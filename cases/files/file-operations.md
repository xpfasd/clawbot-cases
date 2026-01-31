# 文件处理案例

## 场景
使用 ClawBot 处理各种文件操作

## 基本文件操作

### 读取文件

```bash
# 读取文件内容
read file_path:"~/clawbot-cases/README.md"
```

### 写入文件

```bash
# 创建新文件
write file_path:"~/test.txt" content:"Hello World"
```

### 编辑文件

```bash
# 精确替换
edit path:"~/test.txt" oldText:"旧内容" newText:"新内容"
```

## 批量处理案例

### 批量重命名

**对话示例：**
```
用户: 把所有 .txt 文件重命名为 .md
```

**实现：**
```bash
bash command:"

```sh
#!/bin/bash
for file in *.txt; do
    if [ -f \"$file\" ]; then
        mv \"$file\" \"${file%.txt}.md\"
    fi
done
```

"
```

### 文件搜索

```bash
bash command:"

```sh
# 查找所有 Python 文件
find . -name \"*.py\" -type f

# 查找最近7天修改的文件
find . -mtime -7 -type f

# 查找空文件
find . -size 0 -type f
```

"
```

### 文件内容替换

```bash
bash command:"

```sh
# 递归替换目录中所有文件的内容
sed -i 's/旧文本/新文本/g' $(find . -type f)
```

"
```

## 特定格式处理

### JSON 处理

```bash
# 读取并解析 JSON
read file_path:"~/config.json"

# jq 示例
bash command:"cat config.json | jq '.key'"
```

### CSV 处理

```bash
# 查看 CSV
bash command:"

```sh
# 查看前10行
head -n 10 data.csv

# 统计行数
wc -l data.csv

# 按列筛选
awk -F',' '{print $1, $3}' data.csv
```

"
```

### Markdown 处理

```bash
# 转换 Markdown 为 HTML
bash command:"pandoc README.md -o README.html"

# 提取所有标题
bash command:"grep -E '^#{1,6}' README.md"
```

## 文件压缩与解压

```bash
# 压缩
bash command:"

```sh
# tar.gz
tar -czf archive.tar.gz directory/

# zip
zip -r archive.zip directory/
```

"

# 解压
bash command:"

```sh
# tar.gz
tar -xzf archive.tar.gz

# zip
unzip archive.zip
```

"
```

## 文件同步

```bash
# 使用 rclone 同步
bash command:"rclone sync local_dir remote:backup_dir"

# rsync 备份
bash command:"rsync -avz source/ destination/"
```

## 文件位置
`cases/files/file-operations.md`
