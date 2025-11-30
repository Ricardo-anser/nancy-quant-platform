# Nancy 量化平台 API 文档

## 认证

所有 API 端点都需要认证。可以使用以下方式之一进行认证：

1. Token 认证：在请求头中添加 `Authorization: Token <your-token>`
2. Session 认证：通过登录后使用会话

## 用户相关

### 获取当前用户信息

- **URL**: `/api/users/me/`
- **方法**: `GET`
- **描述**: 获取当前登录用户的信息

### 获取/更新用户资料

- **URL**: `/api/users/profile/`
- **方法**: `GET`, `PUT`, `PATCH`
- **描述**: 获取或更新当前用户的资料信息

## 策略相关

### 获取策略列表

- **URL**: `/api/strategies/strategies/`
- **方法**: `GET`
- **描述**: 获取当前用户的所有策略

### 创建策略

- **URL**: `/api/strategies/strategies/`
- **方法**: `POST`
- **描述**: 创建新的策略
- **参数**:
  - `name`: 策略名称
  - `description`: 策略描述
  - `strategy_type`: 策略类型 (technical, fundamental, mixed)
  - `code`: 策略代码
  - `is_public`: 是否公开

### 获取策略详情

- **URL**: `/api/strategies/strategies/<id>/`
- **方法**: `GET`
- **描述**: 获取特定策略的详细信息

### 更新策略

- **URL**: `/api/strategies/strategies/<id>/`
- **方法**: `PUT`, `PATCH`
- **描述**: 更新特定策略的信息

### 删除策略

- **URL**: `/api/strategies/strategies/<id>/`
- **方法**: `DELETE`
- **描述**: 删除特定策略

### 运行策略回测

- **URL**: `/api/strategies/strategies/<id>/run-backtest/`
- **方法**: `POST`
- **描述**: 触发特定策略的回测任务
- **响应**:
  - `task_id`: 任务ID
  - `status`: 任务状态
  - `message`: 消息

## 回测结果相关

### 获取回测结果列表

- **URL**: `/api/strategies/backtest-results/`
- **方法**: `GET`
- **描述**: 获取当前用户的所有回测结果

### 获取回测结果详情

- **URL**: `/api/strategies/backtest-results/<id>/`
- **方法**: `GET`
- **描述**: 获取特定回测结果的详细信息

## 任务状态相关

### 获取任务状态

- **URL**: `/api/strategies/task-status/<task_id>/`
- **方法**: `GET`
- **描述**: 获取特定任务的执行状态
- **响应**:
  - `task_id`: 任务ID
  - `status`: 任务状态 (PENDING, STARTED, SUCCESS, FAILURE, etc.)
  - `result`: 任务结果

## 行情数据相关

### 获取股票列表

- **URL**: `/api/market-data/stocks/`
- **方法**: `GET`
- **描述**: 获取所有股票列表

### 获取股票详情

- **URL**: `/api/market-data/stocks/<id>/`
- **方法**: `GET`
- **描述**: 获取特定股票的详细信息

### 获取股票价格列表

- **URL**: `/api/market-data/prices/`
- **方法**: `GET`
- **描述**: 获取所有股票价格数据

### 获取特定股票的价格列表

- **URL**: `/api/market-data/prices/<symbol>/`
- **方法**: `GET`
- **描述**: 获取特定股票的价格数据

### 获取财务报告列表

- **URL**: `/api/market-data/financial-reports/`
- **方法**: `GET`
- **描述**: 获取所有财务报告数据

### 获取特定股票的财务报告列表

- **URL**: `/api/market-data/financial-reports/<symbol>/`
- **方法**: `GET`
- **描述**: 获取特定股票的财务报告数据