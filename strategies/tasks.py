from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from .models import Strategy, BacktestResult
from market_data.models import DailyPrice
import pandas as pd
import numpy as np
from datetime import datetime

@shared_task
def run_backtest(strategy_id):
    """
    异步运行策略回测
    """
    try:
        # 获取策略对象
        strategy = Strategy.objects.get(id=strategy_id)
        
        # 获取策略相关的股票数据
        # 这里我们假设策略是针对特定股票的，实际应用中可能需要更复杂的逻辑
        prices = DailyPrice.objects.filter(
            stock__symbol=strategy.name  # 假设策略名与股票代码相同
        ).order_by('date')
        
        if not prices.exists():
            raise ValueError("No price data found for this strategy")
        
        # 将数据转换为pandas DataFrame进行处理
        data = pd.DataFrame(list(prices.values('date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume')))
        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)
        
        # 简单的移动平均线策略示例
        # 在实际应用中，这里会是更复杂的策略逻辑
        data['ma_short'] = data['close_price'].rolling(window=5).mean()
        data['ma_long'] = data['close_price'].rolling(window=20).mean()
        data['signal'] = 0
        data['signal'][5:] = np.where(data['ma_short'][5:] > data['ma_long'][5:], 1, 0)
        data['position'] = data['signal'].diff()
        
        # 计算收益
        data['returns'] = data['close_price'].pct_change()
        data['strategy_returns'] = data['position'].shift(1) * data['returns']
        data['cumulative_returns'] = (1 + data['strategy_returns']).cumprod()
        
        # 计算最终收益
        total_return = data['cumulative_returns'].iloc[-1] - 1
        annualized_return = (1 + total_return) ** (252 / len(data)) - 1
        
        # 创建回测结果
        backtest_result = BacktestResult.objects.create(
            strategy=strategy,
            start_date=data.index.min(),
            end_date=data.index.max(),
            total_return=total_return,
            annualized_return=annualized_return,
            max_drawdown=0.0,  # 简化处理，实际应计算最大回撤
            sharpe_ratio=0.0,  # 简化处理，实际应计算夏普比率
            created_at=datetime.now()
        )
        
        return {
            'status': 'success',
            'result_id': backtest_result.id,
            'message': f'Backtest completed for strategy {strategy.name}'
        }
        
    except ObjectDoesNotExist:
        return {
            'status': 'error',
            'message': f'Strategy with id {strategy_id} does not exist'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error running backtest: {str(e)}'
        }