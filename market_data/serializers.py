from rest_framework import serializers
from .models import Stock, DailyPrice, FinancialReport

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = '__all__'

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'