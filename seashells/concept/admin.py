from django.contrib import admin
from .models import CountryTaxesConcept, Tax
from tinymce.models import HTMLField

@admin.register(CountryTaxesConcept)
class CountryTaxesConceptAdmin(admin.ModelAdmin):
    list_display = ('rate_percentage', 'rate_fixed', 'rate_formula', 'country', 'tax')
    list_filter = ('country',)
    search_fields = ('tax', 'country__name')

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')