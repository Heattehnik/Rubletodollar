from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'code', 'name', 'rate', 'date', )
        read_only_fields = ('id',)


class CombinedCurrencySerializer(serializers.Serializer):
    latest_currency = CurrencySerializer()
    last_10_requests = CurrencySerializer(many=True)

    class Meta:
        fields = ('latest_currency', 'last_10_requests',)
