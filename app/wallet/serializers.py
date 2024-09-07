from rest_framework import serializers

from app.wallet.models import Transaction, CsinCoinModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CsinCoinSerializer(serializers.ModelSerializer):
    well = serializers.ReadOnlyField()
    class Meta:
        model = CsinCoinModel
        fields = '__all__'
