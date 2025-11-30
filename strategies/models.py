from django.db import models
from django.contrib.auth.models import User

class Strategy(models.Model):
    STRATEGY_TYPES = [
        ('technical', '技术指标'),
        ('fundamental', '基本面'),
        ('mixed', '混合型'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    strategy_type = models.CharField(max_length=20, choices=STRATEGY_TYPES)
    code = models.TextField(help_text="策略代码")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class BacktestResult(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, related_name='backtest_results')
    start_date = models.DateField()
    end_date = models.DateField()
    initial_capital = models.DecimalField(max_digits=15, decimal_places=2)
    final_value = models.DecimalField(max_digits=15, decimal_places=2)
    total_return = models.FloatField()
    annual_return = models.FloatField()
    max_drawdown = models.FloatField()
    sharpe_ratio = models.FloatField(null=True, blank=True)
    win_rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.strategy.name} - {self.created_at.strftime('%Y-%m-%d')}"