from rest_framework import serializers
from .models import Strategy, BacktestResult

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = '__all__'

class BacktestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = BacktestResult
        fields = '__all__'