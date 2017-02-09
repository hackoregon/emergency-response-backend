from rest_framework import serializers
from data.models import Incident, Agency, AlarmLevel, CensusTract, FireBlock, TypeNatureCode, Station, FireStation, FMA, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident

class TypeNatureCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNatureCode
        fields = ('typenaturecode_id', 'description', 'id_911', 'category', 'nemsis' )

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
        fields = ('gid', 'objectid_1', 'objectid', 'fma', 'resp_zone', 'jurisdict', 'dist_grp', 'notes', 'of_fma', 'mv_label', 'shape_leng', 'shape_area', 'geom')

class FireStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireStation
        fields = ('gid', 'objectid', 'station', 'address', 'city', 'district', 'geom', )

class FMASerializer(serializers.ModelSerializer):
    class Meta:
        model = FMA
        fields = ('gid', 'objectid', 'fma', 'mv_label', 'geom')

# 'shape_star', 'shape_stle',

class MutualAidSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualAid
        fields = ('mutualaid_id', 'description', 'inactive', 'nfirs')

class ResponderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderUnit
        fields = ('responderunit_id', 'description', 'id_911', 'station', 'translateto', 'agency', 'process', 'versaterm')

class IncsitFoundClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFoundClass
        fields = ('incsitfoundclass_id', 'description', 'sortorder')

class IncsitFoundSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFoundSub
        fields = ('incsitfoundsub_id', 'incsitfoundclass', 'description', 'sortorder')

class IncsitFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFound
        fields = ('incsitfound_id', 'incsitfoundsub', 'description', 'statecode', 'sortorder', 'inactive', 'nfirs')

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('incident_id', 'responderunit', 'deptrespond_id', 'runnumber', 'incdate', 'typenaturecode', 'foundsituation', 'incsitfoundprm', 'alarmlevel', 'mutualaid', 'callreceived_id', 'censustract', 'fmarespcomp', 'career', 'engresp', 'aaresp', 'medresp', 'othervehiclesresp', 'firstonscene', 'quad', 'streettype', 'streetname', 'quad2', 'streetname2', 'streettype2', 'city', 'state', 'zip', 'neighborassoc', 'fireblock')
