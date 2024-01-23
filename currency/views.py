from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer, CombinedCurrencySerializer


class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CombinedCurrencySerializer

    def get_queryset(self):
        return Currency.objects.all().order_by('-id')[:1]

