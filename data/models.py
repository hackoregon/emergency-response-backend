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

class AddressGeocode(models.Model):
    rating = models.IntegerField(primary_key=True)
    lon = models.DecimalField(max_digits=13, decimal_places=10)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    stno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    styp =  models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    st = models.CharField(max_length=100)
    zip = models.CharField(max_length=10, blank=True, null=True)

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
    fma = models.ForeignKey(FMA, on_delete=models.CASCADE, blank=True, null=True, related_name='fireblocks', db_column="fma")
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
    id_911 = models.CharField(max_length=15, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    nemsis = models.IntegerField(blank=True, null=True)

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
    station = models.ForeignKey(Station, on_delete=models.CASCADE, blank=True, null=True, related_name='responderunits')
    translateto = models.CharField(max_length=50, blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True, related_name='responderunits')
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
    incsitfoundclass = models.ForeignKey(IncsitFoundClass, on_delete=models.CASCADE, blank=True, null=True, related_name="incsitfoundsubs")
    description = models.CharField(max_length=50, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfoundsub'

class IncsitFound(models.Model):
    incsitfound_id = models.IntegerField(primary_key=True)
    incsitfoundsub = models.ForeignKey(IncsitFoundSub, on_delete=models.CASCADE, blank=True, null=True, related_name="incsitfounds")
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
    incident_id = models.IntegerField(primary_key=True)
    responder_id = models.IntegerField()
    responderunit = models.ForeignKey('ResponderUnit', models.DO_NOTHING, blank=True, null=True)
    codetosc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responder'
        unique_together = [
            ('incident_id', 'responder_id'),
        ]

class IncidentTimes(models.Model):
    inctimes_id = models.IntegerField(primary_key=True)
    timedesc = models.ForeignKey('Timedesc', models.DO_NOTHING, blank=True, null=True)
    incident = models.ForeignKey('Responder', models.DO_NOTHING, blank=True, null=True)
    responder_id = models.IntegerField(blank=True, null=True)
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
