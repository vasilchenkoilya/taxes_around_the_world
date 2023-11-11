from django.contrib import admin
from .models import CountryTaxesConcept

@admin.register(CountryTaxesConcept)
class CountryTaxesConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate_percentage', 'rate_fixed', 'rate_formula', 'country')
    list_filter = ('rate_percentage',)
    search_fields = ('name', 'country__name')