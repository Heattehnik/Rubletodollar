from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
