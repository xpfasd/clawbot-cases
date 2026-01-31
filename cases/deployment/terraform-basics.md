# Terraform 基础设施即代码案例

## 场景
使用 Terraform 管理云基础设施

## 安装

```bash
# 安装 Terraform
brew install terraform

# 或下载二进制文件
wget https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip
unzip terraform_1.7.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

## AWS 配置

```bash
# 配置 AWS 凭证
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="us-east-1"
```

## 基本配置

### Provider 配置

```hcl
# provider.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "default"
}
```

### VPC 配置

```hcl
# vpc.tf
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1a"
  
  tags = {
    Name = "private-subnet"
  }
}
```

### EC2 实例

```hcl
# ec2.tf
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Web server security group"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami               = "ami-0c55b159cbfafe1f0"
  instance_type     = "t2.micro"
  subnet_id         = aws_subnet.public.id
  security_group_ids = [aws_security_group.web.id]
  
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y nginx
              EOF
  
  tags = {
    Name = "web-server"
  }
}
```

### RDS 数据库

```hcl
# rds.tf
resource "aws_db_subnet_group" "main" {
  name       = "main-db-subnet"
  subnet_ids = [aws_subnet.private.id]
}

resource "aws_db_instance" "postgresql" {
  identifier        = "mydb"
  engine            = "postgres"
  engine_version    = "15.2"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  storage_encrypted = true
  
  db_name  = "mydb"
  username = "admin"
  password = "your_password"
  
  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  skip_final_snapshot = true
}
```

## 使用命令

```bash
# 初始化
terraform init

# 规划
terraform plan -out=tfplan

# 应用
terraform apply tfplan

# 查看状态
terraform show

# 销毁
terraform destroy
```

## 远程状态

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

## 文件位置
`cases/deployment/terraform-basics.md`
