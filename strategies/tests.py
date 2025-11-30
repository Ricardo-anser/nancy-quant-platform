from django.test import TestCase
from django.contrib.auth.models import User
from .models import Strategy
from .tasks import run_backtest
from market_data.models import Stock, DailyPrice
from datetime import date, timedelta

class StrategyTestCase(TestCase):
    def setUp(self):
        # 创建测试用户
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # 创建测试股票
        self.stock = Stock.objects.create(
            symbol='TEST',
            name='Test Stock',
            market='SH'
        )
        
        # 创建测试价格数据
        for i in range(30):
            DailyPrice.objects.create(
                stock=self.stock,
                date=date.today() - timedelta(days=30-i),
                open_price=100 + i,
                high_price=105 + i,
                low_price=95 + i,
                close_price=100 + i,
                volume=1000000,
                turnover=10000000,
                adjusted_close=100 + i
            )
        
        # 创建测试策略
        self.strategy = Strategy.objects.create(
            name='TEST',
            description='Test strategy',
            strategy_type='technical',
            code='# Test code',
            author=self.user,
            is_public=False
        )

    def test_run_backtest_task(self):
        """测试运行回测任务"""
        # 运行回测任务
        result = run_backtest(self.strategy.id)
        
        # 检查结果
        self.assertEqual(result['status'], 'success')
        self.assertIn('result_id', result)
        self.assertIn('message', result)
        
    def test_run_backtest_with_invalid_strategy(self):
        """测试运行不存在策略的回测任务"""
        # 运行回测任务，使用不存在的策略ID
        result = run_backtest(99999)
        
        # 检查结果
        self.assertEqual(result['status'], 'error')
        self.assertIn('message', result)