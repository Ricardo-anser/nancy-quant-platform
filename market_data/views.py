from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Stock, DailyPrice, FinancialReport
from .serializers import StockSerializer, DailyPriceSerializer, FinancialReportSerializer

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class DailyPriceListView(generics.ListAPIView):
    serializer_class = DailyPriceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        symbol = self.kwargs.get('symbol')
        if symbol:
            return DailyPrice.objects.filter(stock__symbol=symbol)
        return DailyPrice.objects.all()

class FinancialReportListView(generics.ListAPIView):
    serializer_class = FinancialReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        symbol = self.kwargs.get('symbol')
        if symbol:
            return FinancialReport.objects.filter(stock__symbol=symbol)
        return FinancialReport.objects.all()