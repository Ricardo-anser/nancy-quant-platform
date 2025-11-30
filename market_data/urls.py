from django.urls import path
from . import views

app_name = 'market_data'
urlpatterns = [
    path('stocks/', views.StockListView.as_view(), name='stock-list'),
    path('stocks/<str:symbol>/', views.StockDetailView.as_view(), name='stock-detail'),
    path('prices/', views.DailyPriceListView.as_view(), name='price-list'),
    path('prices/<str:symbol>/', views.DailyPriceListView.as_view(), name='price-list-by-symbol'),
    path('financial-reports/', views.FinancialReportListView.as_view(), name='financial-report-list'),
    path('financial-reports/<str:symbol>/', views.FinancialReportListView.as_view(), name='financial-report-list-by-symbol'),
]