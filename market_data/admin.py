from django.contrib import admin
from .models import Stock, DailyPrice, FinancialReport

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'industry', 'sector', 'market', 'is_active', 'listing_date')
    list_filter = ('market', 'industry', 'sector', 'is_active')
    search_fields = ('symbol', 'name')

@admin.register(DailyPrice)
class DailyPriceAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'close_price', 'volume')
    list_filter = ('date',)
    search_fields = ('stock__symbol', 'stock__name')

@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('stock', 'report_type', 'report_date', 'announcement_date', 'revenue', 'net_profit')
    list_filter = ('report_type', 'report_date')
    search_fields = ('stock__symbol', 'stock__name')