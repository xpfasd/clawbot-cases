# AWS 云服务集成案例

## 场景
使用 ClawBot 集成 AWS 云服务

## AWS 配置

```bash
# 安装 AWS CLI
brew install awscli

# 配置凭证
aws configure
# 或使用环境变量
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="us-east-1"
```

## S3 存储

### 基本操作

```bash
# 列出桶
aws s3 ls

# 创建桶
aws s3 mb s3://my-bucket

# 上传文件
aws s3 cp file.txt s3://my-bucket/

# 下载文件
aws s3 cp s3://my-bucket/file.txt ./

# 同步目录
aws s3 sync local-dir/ s3://my-bucket/

# 删除文件
aws s3 rm s3://my-bucket/file.txt
```

### 公开访问

```bash
# 设置公开访问
aws s3api put-public-access-block \
  --bucket my-bucket \
  --public-access-block-configuration \
  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# 添加桶策略
aws s3api put-bucket-policy \
  --bucket my-bucket \
  --policy file://policy.json
```

## EC2 实例

```bash
# 列出实例
aws ec2 describe-instances \
  --query "Reservations[].Instances[].InstanceId"

# 启动实例
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-12345

# 停止实例
aws ec2 stop-instances --instance-ids i-12345

# 终止实例
aws ec2 terminate-instances --instance-ids i-12345
```

## Lambda 函数

### 创建函数

```bash
# 创建 Lambda 函数
aws lambda create-function \
  --function-name my-function \
  --runtime python3.9 \
  --role arn:aws:iam::123456789:role/lambda-role \
  --handler index.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 300
```

### 调用函数

```bash
# 调用函数
aws lambda invoke \
  --function-name my-function \
  --payload '{"key": "value"}' \
  output.json
```

## DynamoDB

```bash
# 创建表
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions \
    AttributeName=user_id,AttributeType=S \
  --key-schema \
    AttributeName=user_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

# 插入数据
aws dynamodb put-item \
  --table-name Users \
  --item '{"user_id": {"S": "123"}, "name": {"S": "张三"}}'

# 查询数据
aws dynamodb get-item \
  --table-name Users \
  --key '{"user_id": {"S": "123"}}'

# 扫描表
aws dynamodb scan --table-name Users
```

## RDS 数据库

```bash
# 列出数据库实例
aws rds describe-db-instances \
  --query "DBInstances[].DBInstanceIdentifier"

# 创建快照
aws rds create-db-snapshot \
  --db-instance-identifier my-db \
  --db-snapshot-id my-snapshot
```

## ECS 容器

```bash
# 列出集群
aws ecs list-clusters

# 运行任务
aws ecs run-task \
  --cluster my-cluster \
  --task-definition my-task:1 \
  --count 1
```

## SES 邮件

```bash
# 发送邮件
aws ses send-email \
  --from sender@example.com \
  --destination "ToAddresses=recipient@example.com" \
  --message "Subject={Data=Hello}, Body={Text={Data=This is a test email}}"
```

## 文件位置
`cases/cloud/aws-services.md`
