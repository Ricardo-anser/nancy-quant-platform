# 🧠 Nancy 量化选股平台

> 一个基于 **Django + DRF + Celery** 的开源量化投资与策略回测平台，助你轻松构建、测试并管理股票选股策略。

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2%2B-green?logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)

---

## 🗂️ 项目结构

```
nancy-quant-platform/
├── quant_platform/      # Django 项目配置
├── users/               # 用户扩展
├── strategies/          # 策略与回测核心
├── market_data/         # 行情与基本面数据
├── core/                # 工具函数
├── requirements.txt     # 依赖列表
├── .env.example         # 环境变量模板
└── API.md              # API 接口文档
```

## 🌟 核心功能

| 模块 | 功能说明 |
|------|--------|
| 🔐 **用户系统** | 基于 Django Auth，支持注册、登录、权限管理 |
| 📊 **行情数据** | 集成 [AKShare](https://akshare.akfamily.xyz/)，自动获取 A 股日线、财务、指数等数据 |
| 🧪 **策略回测** | 内置 Backtrader 引擎，支持自定义策略逻辑与历史回测 |
| ⏳ **异步任务** | 使用 Celery + Redis 后台执行耗时任务（如回测、数据下载） |
| 🖥️ **管理后台** | 利用 Django Admin 快速管理股票、策略、回测任务 |
| 📡 **RESTful API** | 通过 DRF 提供标准接口，便于前端（Vue/React）对接 |

---

## 🚀 快速开始

### 1️⃣ 克隆项目
```bash
git clone https://github.com/Ricardo-anser/nancy-quant-platform.git
cd nancy-quant-platform
```

### 2️⃣ 创建虚拟环境并安装依赖
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3️⃣ 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填写必要的配置信息
```

### 4️⃣ 数据库配置
确保你已经安装了MySQL数据库，并创建了名为 `nancy_quant_platform_db` 的数据库：
```sql
CREATE DATABASE nancy_quant_platform_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

在 `.env` 文件中配置你的数据库连接信息：
```env
DB_ENGINE=mysql
DB_NAME=nancy_quant_platform_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5️⃣ Redis和Celery配置
确保你已经安装了Redis，并在 `.env` 文件中配置Redis连接信息：
```env
REDIS_URL=redis://localhost:6379/0
```

### 6️⃣ 初始化数据库
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ 创建超级用户
```bash
python manage.py createsuperuser
```

### 8️⃣ 启动开发服务器
```bash
python manage.py runserver
```

### 9️⃣ 启动Celery工作进程
在另一个终端窗口中运行以下命令启动Celery工作进程：
```bash
python celery_worker.py worker --loglevel=info
```

### 🔟 启动Celery Beat调度器（可选）
如果需要定期执行任务（如每日数据更新），可以在另一个终端窗口中运行以下命令启动Celery Beat调度器：
```bash
python celery_beat.py beat --loglevel=info
```

访问 http://127.0.0.1:8000/admin/ 进入管理后台bash
git clone https://github.com/Ricardo-anser/nancy-quant-platform.git
cd nancy-quant-platform