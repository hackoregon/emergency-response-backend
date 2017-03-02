from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis import filters
import django_filters
from data.models import Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FireBlock, CensusBlock, CensusHouseholdIncome, CensusHouseholdLanguage, CensusHousehold65Plus, CensusHousingTenure, CensusMedianHouseholdIncome, CensusRace, CensusTotalPopulation, FcbProportion, FmaShape, TimeDesc, CensusEducationalAttainment
from data.serializers import AgencySerializer, AlarmLevelSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer, MutualAidSerializer, ResponderUnitSerializer, IncsitFoundClassSerializer, IncsitFoundSubSerializer, IncsitFoundSerializer, IncidentSerializer, CensusBlockSerializer, CensusHouseholdIncomeSerializer, CensusHouseholdLanguageSerializer, CensusHousehold65PlusSerializer, CensusHousingTenureSerializer, CensusMedianHouseholdIncomeSerializer, CensusRaceSerializer, CensusTotalPopulationSerializer, FcbProportionSerializer, FmaShapeSerializer, TimeDescSerializer, CensusEducationalAttainmentSerializer


class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    filter_fields = ['agency_id', 'description', 'statecode']

class AlarmLevelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = AlarmLevel.objects.all()
    serializer_class = AlarmLevelSerializer
    filter_fields = '__all__'

class FireBlockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FireBlock.objects.all()
    serializer_class = FireBlockSerializer

class TypeNatureCodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = TypeNatureCode.objects.all()
    serializer_class = TypeNatureCodeSerializer

class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = Station.objects.all()
    serializer_class = StationSerializer

class MutualAidViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = MutualAid.objects.all()
    serializer_class = MutualAidSerializer

class ResponderUnitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = ResponderUnit.objects.all()
    serializer_class = ResponderUnitSerializer

class IncsitFoundClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = IncsitFoundClass.objects.all()
    serializer_class = IncsitFoundClassSerializer

class IncsitFoundSubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = IncsitFoundSub.objects.all()
    serializer_class = IncsitFoundSubSerializer

class IncsitFoundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = IncsitFound.objects.all()
    serializer_class = IncsitFoundSerializer

class IncidentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class CensusBlockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusBlock.objects.all()
    serializer_class = CensusBlockSerializer

class CensusEducationalAttainmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusEducationalAttainment.objects.all()
    serializer_class = CensusEducationalAttainmentSerializer

class CensusHouseholdIncomeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusHouseholdIncome.objects.all()
    serializer_class = CensusHouseholdIncomeSerializer

class CensusHouseholdLanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusHouseholdLanguage.objects.all()
    serializer_class = CensusHouseholdLanguageSerializer

class CensusHousehold65PlusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusHousehold65Plus.objects.all()
    serializer_class = CensusHousehold65PlusSerializer

class CensusHousingTenureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusHousingTenure.objects.all()
    serializer_class = CensusHousingTenureSerializer

class CensusMedianHouseholdIncomeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusMedianHouseholdIncome.objects.all()
    serializer_class = CensusMedianHouseholdIncomeSerializer

class CensusRaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusRace.objects.all()
    serializer_class = CensusRaceSerializer

class CensusTotalPopulationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusTotalPopulation.objects.all()
    serializer_class = CensusTotalPopulationSerializer

class FcbProportionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FcbProportion.objects.all()
    serializer_class = FcbProportionSerializer

class FmaShapeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FmaShape.objects.all()
    serializer_class = FmaShapeSerializer

class TimeDescViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = TimeDesc.objects.all()
    serializer_class = TimeDescSerializer
