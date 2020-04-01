import requests
import xmltodict
from django.core.management.base import BaseCommand

from finance.models import Currency


class Command(BaseCommand):
    def handle(self, **options):
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        sources = xmltodict.parse(r.text)

        for valute in sources['ValCurs']['Valute']:
            currencies = Currency.objects.filter(char_code=valute['CharCode'])
            new_rate = float(valute['Value'].replace(',', '.'))

            if len(currencies) > 0:
                currency = currencies[0]
                currency.rate = new_rate

                currency.save()
            else:
                currency = Currency(
                    source_id=valute['@ID'],
                    char_code=valute['CharCode'],
                    name=valute['Name'],
                    rate=new_rate
                )
                currency.save()
