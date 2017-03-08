from rest_framework import serializers
from rest_framework_gis import serializers
from census.models import CensusBlock, CensusEducationalAttainment

class CensusBlockSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = CensusBlock
        geo_field = "geom"
        auto_bbox = True
        fields = '__all__'

class CensusEducationalAttainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusEducationalAttainment
        fields = '__all__'
