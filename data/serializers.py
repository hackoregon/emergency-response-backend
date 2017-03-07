from rest_framework import serializers
from rest_framework_gis import serializers
from data.models import Incident, Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, CensusBlock, CensusHouseholdIncome, CensusHouseholdLanguage, CensusHousehold65Plus, CensusHousingTenure, CensusMedianHouseholdIncome, CensusRace, CensusTotalPopulation, FcbProportion, FMA, TimeDesc, CensusEducationalAttainment, Responder, IncidentTimes

class TypeNatureCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeNatureCode
        fields = '__all__'

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class AlarmLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmLevel
        fields = '__all__'

class FireBlockSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = FireBlock
        geo_field = "geom"
        auto_bbox = True
        fields = ('gid', 'objectid_1', 'objectid', 'fma', 'resp_zone', 'jurisdict', 'dist_grp', 'notes', 'of_fma', 'mv_label', 'geom')

class MutualAidSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualAid
        fields = '__all__'

class ResponderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderUnit
        fields = '__all__'

class IncsitFoundClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFoundClass
        fields = '__all__'

class IncsitFoundSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFoundSub
        fields = '__all__'

class IncsitFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncsitFound
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class CensusBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusBlock
        fields = '__all__'

class CensusHouseholdIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHouseholdIncome
        fields = '__all__'

class CensusHouseholdLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHouseholdLanguage
        fields = '__all__'

class CensusHousehold65PlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHousehold65Plus
        fields = '__all__'

class CensusHousingTenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusHousingTenure
        fields = '__all__'

class CensusMedianHouseholdIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusMedianHouseholdIncome
        fields = '__all__'

class CensusRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusRace
        fields = '__all__'

class CensusTotalPopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusTotalPopulation
        fields = '__all__'

class FcbProportionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcbProportion
        fields = '__all__'

class FMASerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = FMA
        geo_field = "geom"
        auto_bbox = True
        fields = ('fma', 'geom')

class TimeDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDesc
        fields = '__all__'

class CensusEducationalAttainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusEducationalAttainment
        fields = '__all__'

class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = '__all__'

class IncidentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentTimes
        fields = '__all__'
