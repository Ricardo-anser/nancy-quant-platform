from django.contrib import admin
from .models import Strategy, BacktestResult

@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'strategy_type', 'author', 'is_public', 'created_at')
    list_filter = ('strategy_type', 'is_public', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BacktestResult)
class BacktestResultAdmin(admin.ModelAdmin):
    list_display = ('strategy', 'start_date', 'end_date', 'total_return', 'annual_return', 'max_drawdown', 'created_at')
    list_filter = ('created_at', 'strategy')
    readonly_fields = ('created_at',)