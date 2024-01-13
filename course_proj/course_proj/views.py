from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import StatisticYear, StatisticYearOnlyVac, StatisticCitySalary, StatisticCityPercent, StatisticCityPercentOnlyVac, StatisticCitySalaryOnlyVac

def main_page(request):
    return render(request, "index.html")

def relevance_page(request):
    data_statyear = StatisticYear.objects.all().values()
    data_statyearvac = StatisticYearOnlyVac.objects.all().values()
    return render(request, "relevance.html",
{
            'data_statyear': data_statyear,
            'data_statyearvac': data_statyearvac
        })

def area_page(request):
    data_statcity_salary = StatisticCitySalary.objects.all().values()
    data_statcity_percent = StatisticCityPercent.objects.all().values()
    data_statcity_salary_vac = StatisticCitySalaryOnlyVac.objects.all().values()
    data_statcity_percent_vac = StatisticCityPercentOnlyVac.objects.all().values()
    return render(request, "area.html",
                  {
                      'data_statcity_salary': data_statcity_salary,
                      'data_statcity_percent': data_statcity_percent,
                      'data_statcity_salary_vac':data_statcity_salary_vac,
                      'data_statcity_percent_vac':data_statcity_percent_vac
                  })