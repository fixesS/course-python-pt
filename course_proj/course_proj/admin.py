from django.contrib import admin

from .models import StatisticYear, StatisticYearOnlyVac, StatisticCitySalary, StatisticCitySalaryOnlyVac, StatisticCityPercent, StatisticCityPercentOnlyVac

admin.site.register(StatisticYear)
admin.site.register(StatisticYearOnlyVac)
admin.site.register(StatisticCitySalary)
admin.site.register(StatisticCitySalaryOnlyVac)
admin.site.register(StatisticCityPercent)
admin.site.register(StatisticCityPercentOnlyVac)