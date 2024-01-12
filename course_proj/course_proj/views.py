from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import StatisticYear, StatisticYearOnlyVac

def main_page(request):
    return render(request, "index.html")

def relevance_page(request):
    data_statyear = StatisticYear.objects.all().values()
    data_statyearvac = StatisticYearOnlyVac.objects.all().values()
    return render(request, "relevance.html",
{
            'first_parameter': 'Avg salary',
            'second_parameter': 'Year',
            'data_statyear': data_statyear,
            'data_statyearvac': data_statyearvac
        })