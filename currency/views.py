from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Currency
from .serializers import CurrencySerializer, CombinedCurrencySerializer


class CurrencyView(APIView):
    def get(self, request):
        try:
            latest_currency = Currency.objects.latest('id')
            last_10_requests = Currency.objects.order_by('-id')[:10]

            latest_serializer = CurrencySerializer(latest_currency)
            last_10_serializer = CurrencySerializer(last_10_requests, many=True)

            combined_serializer = CombinedCurrencySerializer({
                'latest_currency': latest_serializer.data,
                'last_10_requests': last_10_serializer.data,
            })

            return Response(combined_serializer.data, status=status.HTTP_200_OK)

        except Currency.DoesNotExist:
            return Response({"error": "No currency data available"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
