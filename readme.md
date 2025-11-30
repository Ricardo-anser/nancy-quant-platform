# 🧠 Nancy 量化选股平台

> 一个基于 **Django + DRF + Celery** 的开源量化投资与策略回测平台，助你轻松构建、测试并管理股票选股策略。

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2%2B-green?logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)

---

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