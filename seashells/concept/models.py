from django.db import models
from cities_light.models import Country

class Tax(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CountryTaxesConcept(models.Model):
    rate_percentage = models.DecimalField(max_digits=20, decimal_places=4, null=True, blank=True)
    rate_fixed = models.DecimalField(max_digits=20, decimal_places=4, null=True, blank=True)
    rate_formula = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, blank=True)




