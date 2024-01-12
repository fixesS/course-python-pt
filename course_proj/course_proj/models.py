from django.db import models


class StatisticYear(models.Model):
    year = models.IntegerField("Год")
    salary_avg = models.IntegerField("Средняя з/п")
    count = models.IntegerField("Количество вакансий")
    objects = models.Manager()
    class Meta:
        db_table = "stat_year"
    pass

class StatisticYearOnlyVac(models.Model):
    year = models.IntegerField("Год")
    salary_avg = models.IntegerField("Средняя з/п")
    count = models.IntegerField("Количество вакансий")
    objects = models.Manager()
    class Meta:
        db_table = "stat_year_only_vac"
    pass

