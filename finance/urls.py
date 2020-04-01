from django.core.exceptions import ObjectDoesNotExist
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from finance.models import Currency
import xmltodict
import requests


@api_view(('GET',))
def get_sources(request):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    sources = xmltodict.parse(r.text)

    return Response({'sources': sources})


@api_view(('GET',))
def get_currencies(request):
    currencies = Currency.objects.all().values()

    return Response({'currencies': currencies})


@api_view(('GET',))
def get_currency(request, id):
    try:
        currency = Currency.objects.values().get(pk=id)
        print(currency)

        return Response({'currency': currency})
    except ObjectDoesNotExist:
        return Response({'currency': None})


@api_view(('GET',))
def get_currencies_by_source_id(request, source_id, page):  # Задачу не понял вот и такое чтото вышло)
    jump = 8
    first = int(page - 1) * jump
    last = first + jump

    currencies = Currency.objects.filter(source_id=source_id)[first:last].values()

    return Response({'currencies': currencies})


urlpatterns = [
    path('currencies/', get_currencies),
    path('currency/<int:id>/', get_currency),
    path('sources/', get_sources),
    path('currencies/<str:source_id>/<int:page>/', get_currencies_by_source_id)
]
