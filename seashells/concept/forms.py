from django import forms
from .models import CountryTaxesConcept

class CountrySelectForm(forms.Form):
    country = forms.ModelChoiceField(queryset=CountryTaxesConcept.objects.all().values_list('country__name', flat=True).distinct())
    
