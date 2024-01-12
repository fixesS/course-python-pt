from django.contrib import admin

from .models import StatisticYear, StatisticYearOnlyVac

admin.site.register(StatisticYear)
admin.site.register(StatisticYearOnlyVac)