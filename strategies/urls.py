from django.urls import path
from . import views

urlpatterns = [
    path('strategies/', views.StrategyListView.as_view(), name='strategy-list'),
    path('strategies/<int:pk>/', views.StrategyDetailView.as_view(), name='strategy-detail'),
    path('strategies/<int:pk>/run-backtest/', views.StrategyDetailView.as_view(), name='strategy-run-backtest'),
    path('backtest-results/', views.BacktestResultListView.as_view(), name='backtest-result-list'),
    path('backtest-results/<int:pk>/', views.BacktestResultDetailView.as_view(), name='backtest-result-detail'),
    path('task-status/<str:task_id>/', views.TaskStatusView.as_view(), name='task-status'),
]