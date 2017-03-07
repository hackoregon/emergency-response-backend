from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class CensusBlock(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    geoid = models.CharField(max_length=12, blank=True, null=True)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceblocks'

class CensusEducationalAttainment(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    no_school_completed = models.IntegerField()
    nursery_school = models.IntegerField()
    kindergarten = models.IntegerField()
    first_grade = models.IntegerField()
    second_grade = models.IntegerField()
    third_grade = models.IntegerField()
    fourth_grade = models.IntegerField()
    fifth_grade = models.IntegerField()
    sixth_grade = models.IntegerField()
    seventh_grade = models.IntegerField()
    eighth_grade = models.IntegerField()
    ninth_grade = models.IntegerField()
    tenth_grade = models.IntegerField()
    eleventh_grade = models.IntegerField()
    twelvth_grade_no_diploma = models.IntegerField()
    regular_hs_diploma = models.IntegerField()
    ged_or_alternative = models.IntegerField()
    some_college_less_than_year = models.IntegerField()
    some_college_more_than_year = models.IntegerField()
    associate_degree = models.IntegerField()
    bachelor_degree = models.IntegerField()
    master_degree = models.IntegerField()
    professional_school_degree = models.IntegerField()
    doctorate_degree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_educational_attainment'
