from django.test import TestCase
from .tasks import sample_task, fetch_market_data, run_backtest

class CoreTasksTestCase(TestCase):
    def test_sample_task(self):
        """测试示例任务"""
        result = sample_task()
        self.assertEqual(result, "Task completed")
        
    def test_fetch_market_data_task(self):
        """测试获取市场数据任务"""
        result = fetch_market_data()
        self.assertEqual(result, "Market data fetched")
        
    def test_run_backtest_task(self):
        """测试运行回测任务"""
        result = run_backtest(1)
        self.assertEqual(result, "Backtest completed for strategy 1")