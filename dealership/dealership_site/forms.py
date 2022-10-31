from django import forms
import calculation
from forex_python.converter import CurrencyRates
from .models import Calc


c = CurrencyRates()

CURRENCY_CHOICES = (
    (c.get_rate('EUR', 'PLN'), "EUR"),
    (c.get_rate('USD', 'PLN'), "USD"),
    (c.get_rate('CHF', 'PLN'), "CHF"),
    (c.get_rate('SEK', 'PLN'), "SEK"),
    (1, "PLN"),
)


class CalcForm(forms.Form):
    buy_price = forms.FloatField()
    exchange = forms.FloatField(choices=CURRENCY_CHOICES, default="PLN")
    transport_costs = forms.FloatField()
    vat = forms.FloatField()

    class Meta:

        model = Calc
        fields = ['buy_price', 'exchange', 'transport_cost', 'vat']