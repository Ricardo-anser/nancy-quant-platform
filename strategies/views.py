from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Strategy, BacktestResult
from .serializers import StrategySerializer, BacktestResultSerializer
from .tasks import run_backtest
from celery.result import AsyncResult

class StrategyListView(generics.ListCreateAPIView):
    serializer_class = StrategySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Strategy.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class StrategyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StrategySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Strategy.objects.filter(author=self.request.user)
    
    @action(detail=True, methods=['post'])
    def run_backtest(self, request, pk=None):
        """触发策略回测"""
        strategy = self.get_object()
        task = run_backtest.delay(strategy.id)
        return Response({
            'task_id': task.id,
            'status': 'Backtest started',
            'message': 'Backtest task has been queued'
        }, status=status.HTTP_202_ACCEPTED)

class BacktestResultListView(generics.ListAPIView):
    serializer_class = BacktestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BacktestResult.objects.filter(strategy__author=self.request.user)

class BacktestResultDetailView(generics.RetrieveAPIView):
    serializer_class = BacktestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BacktestResult.objects.filter(strategy__author=self.request.user)


class TaskStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, task_id):
        task_result = AsyncResult(str(task_id))
        result = {
            'task_id': task_id,
            'status': task_result.status,
            'result': task_result.result
        }
        return Response(result)