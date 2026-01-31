# GCP 云服务集成案例

## 场景
使用 ClawBot 集成 Google Cloud Platform

## 配置

```bash
# 安装 gcloud CLI
brew install google-cloud-sdk

# 初始化
gcloud init

# 设置项目
gcloud config set project my-project

# 认证
gcloud auth login
```

## GCS 存储

```bash
# 列出桶
gsutil ls

# 创建桶
gsutil mb gs://my-bucket

# 上传文件
gsutil cp file.txt gs://my-bucket/

# 下载文件
gsutil cp gs://my-bucket/file.txt ./

# 设置公开访问
gsutil iam ch allUsers:objectViewer gs://my-bucket
```

## Compute Engine

```bash
# 列出实例
gcloud compute instances list

# 创建实例
gcloud compute instances create my-instance \
  --zone=us-central1-a \
  --machine-type=e2-micro

# SSH 连接
gcloud compute ssh my-instance --zone=us-central1-a

# 停止实例
gcloud compute instances stop my-instance --zone=us-central1-a
```

## Cloud Functions

```bash
# 部署函数
gcloud functions deploy my-function \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated

# 调用函数
gcloud functions call my-function \
  --data '{"key": "value"}'

# 列出函数
gcloud functions list
```

## Cloud Run

```bash
# 部署服务
gcloud run deploy my-service \
  --image gcr.io/my-project/my-image \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# 列出服务
gcloud run services list
```

## BigQuery

```bash
# 查询数据
bq query --use_legacy_sql=false \
  "SELECT * FROM \`my-project.dataset.table\` LIMIT 10"

# 加载数据
bq load \
  --source_format=CSV \
  my-project.dataset.table \
  gs://my-bucket/data.csv

# 导出数据
bq extract \
  my-project.dataset.table \
  gs://my-bucket/export-*.csv
```

## Firestore

```bash
# 导出数据
gcloud firestore export gs://my-bucket

# 导入数据
gcloud firestore import gs://my-bucket/export-dir
```

## Pub/Sub

```bash
# 创建主题
gcloud pubsub topics create my-topic

# 创建订阅
gcloud pubsub subscriptions create my-sub \
  --topic=my-topic

# 发布消息
gcloud pubsub topics publish my-topic \
  --message="Hello World"

# 拉取消息
gcloud pubsub subscriptions pull my-sub --auto-ack
```

## Cloud SQL

```bash
# 创建实例
gcloud sql instances create my-instance \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1

# 连接
gcloud sql connect my-instance --user=postgres
```

## Secret Manager

```bash
# 创建密钥
echo "my-secret-value" | gcloud secrets create my-secret --replication-policy=automatic --data-file=-

# 获取密钥
gcloud secrets versions access latest --secret=my-secret
```

## 文件位置
`cases/cloud/gcp-services.md`
