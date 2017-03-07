
class CensusGeographicalMobility(models.Model):
    id = models.CharField(max_length=21)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    total = models.IntegerField()
    same_house_one_yr = models.IntegerField()
    diff_house_us_one_yr = models.IntegerField()
    diff_house_us_one_yr_same_metro = models.IntegerField()
    diff_house_us_one_yr_same_metro_moved_fr_principal_city = models.IntegerField()
    diff_house_us_one_yr_same_metro_moved_fr_rem_metro = models.IntegerField()
    diff_house_us_one_yr_diff_metro_field = models.IntegerField(db_column='diff_house_us_one_yr_diff_metro_')  # Field renamed because it ended with '_'.
    diff_house_us_one_yr_diff_metro_moved_fr_principal_city = models.IntegerField()
    diff_house_us_one_yr_diff_metro_moved_fr_rem_metro = models.IntegerField()
    diff_house_us_one_yr_micro_field = models.IntegerField(db_column='diff_house_us_one_yr_micro_')  # Field renamed because it ended with '_'.
    diff_house_us_one_yr_micro_moved_fr_principal_city = models.IntegerField()
    diff_house_us_one_yr_micro_moved_fr_rem_micro = models.IntegerField()
    diff_house_us_one_yr_not_metro_micro = models.IntegerField()
    abroad_one_yr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_geographical_mobility'


class CensusHealthInsurance(models.Model):
    id = models.CharField(max_length=21)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    with_health_insurance = models.IntegerField()
    no_health_insurance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_health_insurance'

class CensusPovertyStatusIndividuals(models.Model):
    id = models.CharField(max_length=21)
    id2 = models.CharField(max_length=12)
    geography = models.CharField(max_length=60)
    estimate_total = models.IntegerField()
    total_below = models.IntegerField()
    total_above = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'census_poverty_status_individuals'


class FcbProportion(models.Model):
    c_block = models.CharField(max_length=12, blank=True, null=True)
    fire_block = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    overlap_cbg = models.FloatField(blank=True, null=True)
    overlap_fb = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcb_proportion'

class FmacProportion(models.Model):
    c_block = models.CharField(max_length=12, blank=True, null=True)
    fma = models.CharField(max_length=2, blank=True, null=True)
    overlap_cbg = models.FloatField(blank=True, null=True)
    overlap_fma = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fmac_proportion'

class Inctimes(models.Model):
    inctimes_id = models.IntegerField(primary_key=True)
    timedesc = models.ForeignKey('Timedesc', models.DO_NOTHING, blank=True, null=True)
    incident = models.ForeignKey('Responder', models.DO_NOTHING, blank=True, null=True)
    responder_id = models.IntegerField(blank=True, null=True)
    realtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inctimes'


class OrHolidays(models.Model):
    date = models.DateField()
    holiday = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'or_holidays'


class Responder(models.Model):
    incident_id = models.IntegerField()
    responder_id = models.IntegerField()
    responderunit = models.ForeignKey('Responderunit', models.DO_NOTHING, blank=True, null=True)
    codetosc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responder'
        unique_together = (('incident_id', 'responder_id'),)


class Responderunit(models.Model):
    responderunit_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=6, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)
    station = models.ForeignKey('Station', models.DO_NOTHING, blank=True, null=True)
    translateto = models.CharField(max_length=4, blank=True, null=True)
    agency = models.ForeignKey(Agency, models.DO_NOTHING, blank=True, null=True)
    process = models.IntegerField(blank=True, null=True)
    versaterm = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responderunit'


class Situationfound(models.Model):
    situationfound_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nemsis = models.IntegerField(blank=True, null=True)
    e09_15 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situationfound'


class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Timedesc(models.Model):
    timedesc_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timedesc'


class Tl201641Bg(models.Model):
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
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl_2016_41_bg'
