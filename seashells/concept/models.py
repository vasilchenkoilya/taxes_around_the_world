from django.db import models
from cities_light.models import Country


class CountryTaxesConcept(models.Model):
    name = models.CharField(max_length=100)
    rate_percentage = models.DecimalField(max_digits=20, decimal_places=4)
    rate_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    rate_formula = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)



