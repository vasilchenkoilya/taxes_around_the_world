from django.db import models
from cities_light.models import Country


class CountryTaxesConcept(models.Model):
    name = models.CharField(max_length=100)
    rate_percentage = models.DecimalField()
    rate_fixed = models.DecimalField()
    rate_formula = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)



