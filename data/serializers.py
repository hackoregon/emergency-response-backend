from rest_framework import serializers
from data.models import Incident, Agency, AlarmLevel, CensusTract, FireBlock, TypeNatureCode, Station, FireStation

class TypeNatureCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNatureCode
        fields = ('typenaturecode_id', 'description', 'id_911', 'category', 'nemsis' )

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('incident_id', 'responderunit_id', 'runnumber', 'alarmlevel_id', 'mutualaid_id', 'fmarespcomp', 'fireblock', 'neighborassoc', 'censustract', 'quad', 'streetname', 'streettype', 'quad2', 'streetname2', 'streettype2', 'county', 'city', 'state', 'zip', 'incdate', 'typenaturecode_id', 'incsitfoundprm_id')

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('agency_id', 'description', 'statecode')

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('station_id', 'description')

class AlarmLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmLevel
        fields = ('alarmlevel_id', 'description', 'id_911')

class CensusTractSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusTract
        fields = ('gid', 'statefp', 'countyfp', 'tractce', 'blkgrpce', 'geoid', 'namelsad', 'mtfcc', 'funcstat', 'aland', 'awater', 'intptlat', 'intptlon', 'geom')

class FireBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireBlock
        fields = ('gid', 'objectid_1', 'objectid', 'fma', 'resp_zone', 'jurisdict', 'dist_grp', 'notes', 'of_fma', 'mv_label', 'shape_star', 'shape_stle', 'shape_leng', 'shape_area', 'geom')

class FireStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireStation
        fields = ('gid', 'objectid', 'station')
#
# gid = models.AutoField(primary_key=True)
# objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
# station = models.CharField(max_length=6, blank=True, null=True)
# address = models.CharField(max_length=38, blank=True, null=True)
# city = models.CharField(max_length=28, blank=True, null=True)
# district = models.CharField(max_length=40, blank=True, null=True)
# geom =
