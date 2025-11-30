from django.test import TestCase
from django.contrib.auth.models import User
from .models import Stock, DailyPrice, FinancialReport
from datetime import date

class MarketDataTestCase(TestCase):
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
        self.daily_price = DailyPrice.objects.create(
            stock=self.stock,
            date=date.today(),
            open_price=100.00,
            high_price=105.00,
            low_price=95.00,
            close_price=100.50,
            volume=1000000,
            turnover=10000000,
            adjusted_close=100.50
        )
        
        # 创建测试财务报告
        self.financial_report = FinancialReport.objects.create(
            stock=self.stock,
            report_type='annual',
            report_date=date.today(),
            announcement_date=date.today(),
            revenue=10000000,
            net_profit=1000000,
            total_assets=50000000,
            total_liabilities=30000000,
            equity=20000000,
            eps=1.00,
            roe=0.05
        )

    def test_stock_creation(self):
        """测试股票创建"""
        self.assertEqual(self.stock.symbol, 'TEST')
        self.assertEqual(self.stock.name, 'Test Stock')
        self.assertEqual(self.stock.market, 'SH')
        
    def test_daily_price_creation(self):
        """测试日线价格创建"""
        self.assertEqual(self.daily_price.stock, self.stock)
        self.assertEqual(self.daily_price.open_price, 100.00)
        self.assertEqual(self.daily_price.close_price, 100.50)
        
    def test_financial_report_creation(self):
        """测试财务报告创建"""
        self.assertEqual(self.financial_report.stock, self.stock)
        self.assertEqual(self.financial_report.report_type, 'annual')
        self.assertEqual(self.financial_report.revenue, 10000000)