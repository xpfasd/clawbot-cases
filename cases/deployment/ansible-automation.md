# Ansible 自动化运维案例

## 场景
使用 Ansible 进行自动化配置管理

## 安装

```bash
# macOS
brew install ansible

# Ubuntu
sudo apt update
sudo apt install ansible

# 验证
ansible --version
```

## 配置

```bash
# 配置 SSH 免密登录
ssh-copy-id user@server.com

# 创建 inventory
cat > inventory.ini << EOF
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com

[all:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/id_rsa
EOF
```

## Playbook 示例

### 基础 Playbook

```yaml
# site.yml
---
- name: Web 服务器配置
  hosts: webservers
  become: yes
  vars:
    nginx_port: 80
  
  tasks:
    - name: 安装 Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: 启动 Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: 配置防火墙
      ufw:
        state: enabled
        policy: allow
    
    - name: 开放 80 端口
      ufw:
        rule: allow
        port: '{{ nginx_port }}'
        proto: tcp

- name: 数据库服务器配置
  hosts: dbservers
  become: yes
  
  tasks:
    - name: 安装 PostgreSQL
      apt:
        name: postgresql
        state: present
```

### 角色 Playbook

```yaml
# site.yml
---
- name: 生产环境部署
  hosts: all
  roles:
    - common
    - nginx
    - docker
    - monitoring
```

### 创建角色

```bash
# 创建角色结构
ansible-galaxy init roles/nginx

# 角色结构
roles/nginx/
├── tasks/
│   └── main.yml
├── handlers/
│   └── main.yml
├── templates/
│   └── nginx.conf.j2
├── files/
│   └── nginx.pem
├── vars/
│   └── main.yml
├── defaults/
│   └── main.yml
└── meta/
    └── main.yml
```

### Role Tasks

```yaml
# roles/nginx/tasks/main.yml
---
- name: 安装 Nginx
  apt:
    name: nginx
    state: present

- name: 复制配置文件
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Restart Nginx

- name: 启用站点
  template:
    src: site.conf.j2
    dest: /etc/nginx/sites-available/{{ item }}
    mode: '0644'
  loop:
    - default
    - app
  notify: Restart Nginx

- name: 链接站点
  file:
    src: /etc/nginx/sites-available/{{ item }}
    dest: /etc/nginx/sites-enabled/{{ item }}
    state: link
  loop:
    - default
    - app
```

### Handlers

```yaml
# roles/nginx/handlers/main.yml
---
- name: Restart Nginx
  service:
    name: nginx
    state: restarted

- name: Reload Nginx
  service:
    name: nginx
    state: reloaded
```

### 变量

```yaml
# roles/nginx/defaults/main.yml
---
nginx_port: 80
nginx_workers: 4
nginx_max_connections: 1024
nginx_enable_ssl: true

# roles/nginx/vars/main.yml
---
nginx_package: nginx-extras
```

## 常用模块

```yaml
# 文件操作
- name: 创建目录
  file:
    path: /opt/myapp
    state: directory
    mode: '0755'

- name: 复制文件
  copy:
    src: files/config.yml
    dest: /opt/myapp/config.yml
    owner: app
    group: app
    mode: '0644'

- name: 模板渲染
  template:
    src: app.conf.j2
    dest: /opt/myapp/app.conf
    validate: /usr/sbin/nginx -t -c %s

# 服务管理
- name: 启动服务
  service:
    name: myapp
    state: started
    enabled: yes

# 包管理
- name: 安装软件包
  apt:
    name:
      - python3
      - git
      - curl
    state: present

# 用户管理
- name: 创建用户
  user:
    name: deploy
    shell: /bin/bash
    groups: sudo
    append: yes

# Git
- name: 克隆代码
  git:
    repo: https://github.com/example/app.git
    dest: /opt/myapp
    version: main
    force: yes
```

## 文件位置
`cases/deployment/ansible-automation.md`
