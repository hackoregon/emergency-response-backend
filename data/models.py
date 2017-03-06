# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models


class Agency(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=34)
    statecode = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'agency'

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'

class AlarmLevel(models.Model):
    alarmlevel_id = models.IntegerField(primary_key=True)
    description = models.IntegerField()
    id_911 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alarmlevel'

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
    id2 = models.BigIntegerField()
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

class CensusHouseholdIncome(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()
    total_less_than_10000 = models.IntegerField()
    total_10000_to_14999 = models.IntegerField()
    total_15000_to_19999 = models.IntegerField()
    total_20000_to_24999 = models.IntegerField()
    total_25000_to_29999 = models.IntegerField()
    total_30000_to_34999 = models.IntegerField()
    total_35000_to_39999 = models.IntegerField()
    total_40000_to_44999 = models.IntegerField()
    total_45000_to_49999 = models.IntegerField()
    total_50000_to_59999 = models.IntegerField()
    total_60000_to_74999 = models.IntegerField()
    total_75000_to_99999 = models.IntegerField()
    total_100000_to_124999 = models.IntegerField()
    total_125000_to_149999 = models.IntegerField()
    total_150000_to_199999 = models.IntegerField()
    total_200000_or_more = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_household_income'

class CensusHouseholdLanguage(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()
    english_only = models.IntegerField()
    spanish_total = models.IntegerField()
    spanish_lesh = models.IntegerField()
    spanish_notlesh = models.IntegerField()
    other_indo_euro_total = models.IntegerField()
    other_indo_euro_lesh = models.IntegerField()
    other_indo_euro_notlesh = models.IntegerField()
    asian_pacific_island_total = models.IntegerField()
    asian_pacific_island_lesh = models.IntegerField()
    asian_pacific_island_notlesh = models.IntegerField()
    other_total = models.IntegerField()
    other_lesh = models.IntegerField()
    other_notlesh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_household_language'


class CensusHousehold65Plus(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    totals = models.IntegerField()
    oneplus_people_65plus = models.IntegerField()
    one_or_more_people_65plus_1_person = models.IntegerField()
    oneplus_people_65plus_2plus_person = models.IntegerField()
    oneplus_people_65plus_2plus_person_family = models.IntegerField()
    oneplus_people_65plus_2plus_person_nonfamily = models.IntegerField()
    no_people_65plus = models.IntegerField()
    no_people_65plus_1_person = models.IntegerField()
    no_people_65plus_2plus_person = models.IntegerField()
    no_people_65plus_2plus_person_family = models.IntegerField()
    no_people_65plus_2plus_person_nonfamily = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_households_65plus'


class CensusHousingTenure(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total_households = models.IntegerField()
    estimate_total_owner_occupied = models.IntegerField()
    estimate_total_renter_occupied = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_housing_tenure'


class CensusMedianHouseholdIncome(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_median_household_income = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_median_household_income'


class CensusRace(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    white_alone = models.IntegerField()
    black_alone = models.IntegerField()
    american_indian_alaska_native_alone = models.IntegerField()
    asian_alone = models.IntegerField()
    native_hawaiian_pacific_islander_alone = models.IntegerField()
    some_other_alone = models.IntegerField()
    two_or_more_races = models.IntegerField()
    two_or_more_some_other = models.IntegerField()
    two_or_more_excluding_some_other_three_or_more_races = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_race'


class CensusTotalPopulation(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_total_population'

class FcbProportion(models.Model):
    c_block = models.CharField(max_length=12, blank=True, null=True)
    fire_block = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    overlap_cbg = models.FloatField(blank=True, null=True)
    overlap_fb = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcb_proportion'

class FMA(models.Model):
    fma = models.CharField(max_length=2, primary_key=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fma_shapes'

class FireBlock(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fma = models.CharField(max_length=2, blank=True, null=True)
    resp_zone = models.CharField(max_length=6, blank=True, null=True)
    jurisdict = models.CharField(max_length=2, blank=True, null=True)
    dist_grp = models.CharField(max_length=2, blank=True, null=True)
    notes = models.CharField(max_length=60, blank=True, null=True)
    of_fma = models.CharField(max_length=26, blank=True, null=True)
    mv_label = models.CharField(max_length=15, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fblocks'

class TypeNatureCode(models.Model):
    typenaturecode_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=8, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    nemsis = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typenaturecode'

class MutualAid(models.Model):
    mutualaid_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nfirs = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mutualaid'

class ResponderUnit(models.Model):
    responderunit_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, blank=True, null=True)
    translateto = models.CharField(max_length=50, blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)
    process = models.IntegerField(blank=True, null=True)
    versaterm = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responderunit'

class IncsitFoundClass(models.Model):
    incsitfoundclass_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfoundclass'

class IncsitFoundSub(models.Model):
    incsitfoundsub_id = models.IntegerField(primary_key=True)
    incsitfoundclass = models.ForeignKey(IncsitFoundClass, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfoundsub'

class IncsitFound(models.Model):
    incsitfound_id = models.IntegerField(primary_key=True)
    incsitfoundsub = models.ForeignKey(IncsitFoundSub, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    statecode = models.CharField(max_length=3, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nfirs = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfound'

class Incident(models.Model):
    incident_id = models.IntegerField(primary_key=True)
    responderunit = models.ForeignKey(ResponderUnit, on_delete=models.CASCADE, blank=True, null=True)
    deptrespond_id = models.IntegerField(blank=True, null=True)
    runnumber = models.CharField(max_length=20, blank=True, null=True)
    incdate = models.DateField(blank=True, null=True)
    typenaturecode = models.ForeignKey('Typenaturecode', models.DO_NOTHING, blank=True, null=True)
    foundsituation = models.IntegerField(blank=True, null=True)
    incsitfoundprm = models.ForeignKey('Incsitfound', models.DO_NOTHING, blank=True, null=True)
    alarmlevel = models.ForeignKey('AlarmLevel', models.DO_NOTHING, blank=True, null=True)
    mutualaid = models.ForeignKey('Mutualaid', models.DO_NOTHING, blank=True, null=True)
    callreceived_id = models.IntegerField(blank=True, null=True)
    censustract = models.CharField(max_length=6, blank=True, null=True)
    fmarespcomp = models.CharField(max_length=10, blank=True, null=True)
    career = models.IntegerField(blank=True, null=True)
    engresp = models.IntegerField(blank=True, null=True)
    aaresp = models.IntegerField(blank=True, null=True)
    medresp = models.IntegerField(blank=True, null=True)
    othervehiclesresp = models.IntegerField(blank=True, null=True)
    firstonscene = models.CharField(max_length=10, blank=True, null=True)
    quad = models.CharField(max_length=2, blank=True, null=True)
    streettype = models.CharField(max_length=4, blank=True, null=True)
    streetname = models.CharField(max_length=30, blank=True, null=True)
    quad2 = models.CharField(max_length=4, blank=True, null=True)
    streetname2 = models.CharField(max_length=30, blank=True, null=True)
    streettype2 = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    neighborassoc = models.CharField(max_length=20, blank=True, null=True)
    fireblock = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident'

class TimeDesc(models.Model):
    timedesc_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timedesc'

class Responder(models.Model):
    incident_id = models.IntegerField()
    responder_id = models.IntegerField()
    responderunit_id = models.ForeignKey(ResponderUnit, on_delete=models.CASCADE, blank=True, null=True)
    codetosc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responder'
        unique_together = (('incident_id', 'responder_id'),)

class IncTimes(models.Model):
    inctimes_id = models.IntegerField(primary_key=True)
    timedesc_id = models.ForeignKey(TimeDesc, on_delete=models.CASCADE, blank=True, null=True)
    incident_id = models.ForeignKey(Incident, on_delete=models.CASCADE, blank=True, null=True)
    responder_id = models.ForeignKey(Responder, on_delete=models.CASCADE, blank=True, null=True)
    realtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inctimes'

class SituationFound(models.Model):
    situationfound_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nemsis = models.CharField(max_length=10, blank=True, null=True)
    e09_15 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situationfound'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
