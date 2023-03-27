from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    acquisition_date = models.DateField(null=True)
    number_3l_code = models.CharField(max_length=3)
    deal_type_id = models.CharField(max_length=10)
    group_id = models.CharField(max_length=10)
    status_id = models.CharField(max_length=20)
    company_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class WTG(models.Model):
    wtg_number = models.CharField(max_length=50, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    type_id = models.CharField(max_length=20)
    region_id = models.CharField(max_length=50)
    kw = models.IntegerField()
    hub = models.IntegerField()
    rotor = models.IntegerField()
    altitude = models.IntegerField(null=True)
    cod = models.DateField(null=True)
    zip_code = models.IntegerField()
    wgs_84_north = models.FloatField()
    wgs_84_east = models.FloatField()
    gauss_krueger_zone = models.IntegerField()
    gauss_krueger_north = models.FloatField()
    gauss_krueger_east = models.FloatField()
    town_id = models.CharField(max_length=255)

    def __str__(self):
        return self.wtg_number
