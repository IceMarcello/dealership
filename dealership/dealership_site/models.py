from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from forex_python.converter import CurrencyRates

STATUS_CHOICES = (
    ("AVAILABLE", "AVAILABLE"),
    ("SOLD", "SOLD"),
)
FUEL_CHOICES = (
    ("Diesel", "Diesel"),
    ("Gas", "Gas"),
    ("Hybrid", "Hybrid"),
    ("Electric", "Electric"),
    ("Other", "Other"),
)

c = CurrencyRates()

CURRENCY_CHOICES = (
    (c.get_rate('EUR', 'PLN'), "EUR"),
    (c.get_rate('USD', 'PLN'), "USD"),
    (c.get_rate('CHF', 'PLN'), "CHF"),
    (c.get_rate('SEK', 'PLN'), "SEK"),
    (1, "PLN"),
)


class Post(models.Model):
    title = models.CharField(max_length=22)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    content = models.TextField()
    price = models.IntegerField()
    odo = models.BigIntegerField()
    capacity = models.IntegerField()
    power = models.FloatField()
    year = models.IntegerField()
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICES, default="Other")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="AVAILABLE")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Calc(models.Model):
    title = models.CharField(max_length=200)
    buy_price = models.FloatField()
    exchange = models.FloatField(choices=CURRENCY_CHOICES, default=1)
    transport_cost = models.FloatField()
    vat = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def calc_costs(self):
        return float(self.buy_price * self.exchange + self.transport_cost + self.buy_price * self.exchange * self.vat)

