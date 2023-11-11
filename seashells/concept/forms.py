from django import forms
from .models import CountryTaxesConcept

class CountrySelectForm(forms.Form):
    country_choices = [(country.name, country.name) for country in CountryTaxesConcept.objects.all()]
    country = forms.ChoiceField(choices=country_choices)
    
