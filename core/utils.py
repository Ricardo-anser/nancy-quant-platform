import pandas as pd
import numpy as np
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

def calculate_returns(prices: List[float]) -> List[float]:
    """
    计算收益率序列
    """
    returns = []
    for i in range(1, len(prices)):
        if prices[i-1] != 0:
            ret = (prices[i] - prices[i-1]) / prices[i-1]
            returns.append(ret)
        else:
            returns.append(0)
    return returns

def calculate_max_drawdown(returns: List[float]) -> float:
    """
    计算最大回撤
    """
    cumulative = np.cumprod([1 + r for r in returns])
    running_max = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - running_max) / running_max
    return abs(min(drawdown)) if len(drawdown) > 0 else 0

def calculate_sharpe_ratio(returns: List[float], risk_free_rate: float = 0.02) -> float:
    """
    计算夏普比率
    """
    if len(returns) == 0:
        return 0
    
    excess_returns = [r - risk_free_rate/252 for r in returns]  # 假设252个交易日
    mean_excess_return = np.mean(excess_returns)
    std_dev = np.std(excess_returns)
    
    if std_dev == 0:
        return 0
    
    return mean_excess_return / std_dev * np.sqrt(252)

def normalize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    标准化数据格式
    """
    normalized = {}
    for key, value in data.items():
        if isinstance(value, pd.Timestamp):
            normalized[key] = value.isoformat()
        elif isinstance(value, np.integer):
            normalized[key] = int(value)
        elif isinstance(value, np.floating):
            normalized[key] = float(value)
        elif isinstance(value, np.ndarray):
            normalized[key] = value.tolist()
        else:
            normalized[key] = value
    return normalized