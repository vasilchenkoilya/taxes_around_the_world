from django.shortcuts import render
from .forms import CountrySelectForm
from .models import CountryTaxesConcept

def index(request):
    return render(request, 'concept/index.html')

def compare_countries_view(request):
    if request.method == 'POST':
        form1 = CountrySelectForm(request.POST, prefix='country1')
        form2 = CountrySelectForm(request.POST, prefix='country2')
        if form1.is_valid() and form2.is_valid():
            country1 = CountryTaxesConcept.objects.filter(country__name=form1.cleaned_data['country'])
            country2 = CountryTaxesConcept.objects.filter(country__name=form2.cleaned_data['country'])
            return render(request, 'concept/comparing.html', {'country1': country1, 'country2': country2})
    else:
        form1 = CountrySelectForm(prefix='country1')
        form2 = CountrySelectForm(prefix='country2')
    return render(request, 'concept/comparing.html', {'form1': form1, 'form2': form2})