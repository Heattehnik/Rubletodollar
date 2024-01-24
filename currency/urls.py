from django.urls import path
from currency.apps import CurrencyConfig
from currency.views import CurrencyView

app_name = CurrencyConfig.name

urlpatterns = [
    path('get-current-usd/', CurrencyView.as_view(), name='currency'),
]
