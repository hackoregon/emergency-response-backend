from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField
from data.models import Incident, Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FMA, TimeDesc, Responder, IncidentTimes, SituationFound, FMAStats

# add AddressGeocode import to models if using geocoder

# class AddressGeocodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddressGeocode
#         fields = '__all__'

class TypeNatureCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNatureCode
        fields = '__all__'

class AlarmLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmLevel
        fields = '__all__'

class FMAFireBlockFireBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireBlock
        fields = ('gid',)

class FireBlockSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = FireBlock
        geo_field = "geom"
        auto_bbox = True
        fields = ('gid', 'objectid_1', 'objectid', 'fma', 'resp_zone', 'jurisdict', 'dist_grp', 'notes', 'of_fma', 'mv_label', 'geom')

class FMAFireBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireBlock
        fields = ('gid',)

class FMASerializer(serializers.GeoFeatureModelSerializer):
    # fireblocks = FMAFireBlockSerializer(many=True)
    fma_id = CharField(source='fma')
    class Meta:
        model = FMA
        geo_field = "geom"
        auto_bbox = True
        id_field = False
        fields = ('geom', 'fma_id')

class FMAStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FMAStats
        exclude = ('fma',)

class MutualAidSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualAid
        fields = '__all__'

class ResponderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderUnit
        fields = '__all__'

class ForeignResponderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderUnit
        fields = ('responderunit_id', 'description', 'id_911', 'translateto', 'agency', 'process', 'versaterm')

class StationSerializer(serializers.ModelSerializer):
    responderunits = ForeignResponderUnitSerializer(many=True)
    class Meta:
        model = Station
        fields = ('station_id', 'description', 'responderunits')
        depth = 2

class AgencySerializer(serializers.ModelSerializer):
    name = CharField(source='description')
    responderunits = ForeignResponderUnitSerializer(many=True)
    class Meta:
        model = Agency
        fields = ('agency_id', 'name', 'statecode', 'responderunits')

class IncsitFoundClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFoundClass
        fields = ('incsitfoundclass_id', 'description', 'sortorder')

class IncsitFoundSubSerializer(serializers.ModelSerializer):
    incitfoundclasses = IncsitFoundClassSerializer(many=True)
    class Meta:
        model = IncsitFoundSub
        fields = '__all__'

class IncsitFoundSerializer(serializers.ModelSerializer):
    # incsitfoundsubs = IncsitFoundSubSerializer(many=True)
    class Meta:
        model = IncsitFound
        fields = ('incsitfound_id', 'statecode', 'sortorder', 'inactive', 'nfirs')

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('incident_id', 'responderunit', 'deptrespond_id', 'runnumber', 'incdate', 'typenaturecode', 'foundsituation', 'incsitfoundprm', 'alarmlevel', 'callreceived_id', 'censustract', 'fmarespcomp', 'career', 'engresp', 'aaresp', 'medresp', 'othervehiclesresp', 'firstonscene', 'quad', 'streettype', 'streetname', 'quad2', 'streettype', 'streetname', 'quad2', 'streetname2', 'streettype2', 'city', 'state', 'zip', 'neighborassoc', 'fireblock')

class TimeDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDesc
        fields = '__all__'

class IncidentResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = ('responder_id', 'responderunit', 'codetosc')

class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = '__all__'

class IncidentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentTimes
        fields = '__all__'

class IncidentIncidentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentTimes
        fields = ('inctimes_id','timedesc', 'responder_id','realtime')

class SituationFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationFound
        fields = '__all__'
