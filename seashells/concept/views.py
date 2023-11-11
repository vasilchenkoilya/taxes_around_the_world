from django.shortcuts import render
from .models import CountryTaxesConcept


def index(request):
    countries = CountryTaxesConcept.objects.values_list('country__name', flat=True).distinct()
    print(countries)
    return render(request, 'concept/index.html', {'countries': countries})

def compare_view(request):
    country1 = request.GET.get('country1')
    country2 = request.GET.get('country2')

    taxes1 = CountryTaxesConcept.objects.filter(country__name=country1)
    taxes2 = CountryTaxesConcept.objects.filter(country__name=country2)
    taxes = zip(taxes1, taxes2)

    context = {
        'taxes': taxes,
        'country1': country1,
        'country2': country2
    }

    return render(request, 'concept/compare.html', context)

