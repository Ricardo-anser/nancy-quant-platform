from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True, help_text="股票代码")
    name = models.CharField(max_length=100, help_text="股票名称")
    industry = models.CharField(max_length=50, blank=True, null=True, help_text="所属行业")
    sector = models.CharField(max_length=50, blank=True, null=True, help_text="所属板块")
    listing_date = models.DateField(blank=True, null=True, help_text="上市日期")
    market = models.CharField(max_length=10, choices=[('SH', '沪市'), ('SZ', '深市')], help_text="交易市场")
    is_active = models.BooleanField(default=True, help_text="是否仍在交易")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.symbol} - {self.name}"

class DailyPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField(help_text="交易日期")
    open_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="开盘价")
    high_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="最高价")
    low_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="最低价")
    close_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="收盘价")
    volume = models.BigIntegerField(help_text="成交量")
    turnover = models.DecimalField(max_digits=15, decimal_places=2, help_text="成交额")
    adjusted_close = models.DecimalField(max_digits=10, decimal_places=2, help_text="复权收盘价")
    
    class Meta:
        unique_together = ('stock', 'date')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"

class FinancialReport(models.Model):
    REPORT_TYPES = [
        ('quarterly', '季度报告'),
        ('annual', '年度报告'),
    ]
    
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='financial_reports')
    report_type = models.CharField(max_length=10, choices=REPORT_TYPES, help_text="报告类型")
    report_date = models.DateField(help_text="报告期")
    announcement_date = models.DateField(help_text="公告日期")
    
    # 主要财务指标
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text="营业收入")
    net_profit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text="净利润")
    total_assets = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text="总资产")
    total_liabilities = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text="总负债")
    equity = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text="股东权益")
    eps = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="每股收益")
    roe = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="净资产收益率")
    
    class Meta:
        unique_together = ('stock', 'report_type', 'report_date')
    
    def __str__(self):
        return f"{self.stock.symbol} - {self.report_type} - {self.report_date}"