from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'code', 'name', 'rate', 'date', )
        read_only_fields = ('id',)


class CombinedCurrencySerializer(serializers.Serializer):
    latest_currency = serializers.SerializerMethodField()
    last_10_requests = serializers.SerializerMethodField()

    class Meta:
        fields = ('latest_currency', 'last_10_currencies',)

    def get_latest_currency(self, obj):
        latest_currency = Currency.objects.latest('id')
        serializer = CurrencySerializer(latest_currency)
        return serializer.data

    def get_last_10_requests(self, obj):
        last_10_requests = Currency.objects.order_by('-id')[:10]
        serializer = CurrencySerializer(last_10_requests, many=True)
        return serializer.data
