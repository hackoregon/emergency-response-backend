from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from django.contrib.gis.geos import Point
from data.models import Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FireBlock, CensusBlock, CensusHouseholdIncome, CensusHouseholdLanguage, CensusHousehold65Plus, CensusHousingTenure, CensusMedianHouseholdIncome, CensusRace, CensusTotalPopulation, FcbProportion, FMA, TimeDesc, CensusEducationalAttainment
from data.serializers import AgencySerializer, AlarmLevelSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer, MutualAidSerializer, ResponderUnitSerializer, IncsitFoundClassSerializer, IncsitFoundSubSerializer, IncsitFoundSerializer, IncidentSerializer, CensusBlockSerializer, CensusHouseholdIncomeSerializer, CensusHouseholdLanguageSerializer, CensusHousehold65PlusSerializer, CensusHousingTenureSerializer, CensusMedianHouseholdIncomeSerializer, CensusRaceSerializer, CensusTotalPopulationSerializer, FcbProportionSerializer, FMASerializer, TimeDescSerializer, CensusEducationalAttainmentSerializer

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

class FireBlockListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FireBlock.objects.all()
    serializer_class = FireBlockSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys() #get the keys from url
        filter_dict = {}  #create empty dictonary to hold values
        if(k): # checks if keys exist
            for key, value in request.GET.items(): # loops through all keys
                filter_dict[key] = value # adds the values =  filter type of object
            fireblocks = FireBlock.objects.filter(**filter_dict) #returns the fireblocks filtered by selection
            serialized_fireblocks = FireBlockSerializer(fireblocks, many=True) # return the serialized firblock objects
            return Response(serialized_fireblocks.data) #returns to client
        else:
            return Response(FireBlockSerializer(FireBlock.objects.all(),many=True).data) # if no keys, returns unfiltered list of incidents

class FireBlockGeoFilterViewSet(generics.ListAPIView):

    queryset = FireBlock.objects.all
    serializer_class = FireBlockSerializer

    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat', ' '))
        lon = float(request.GET.get('lon', ' '))
        fireblocks = FireBlock.objects.all
        if lat != ' ' and lon != ' ':
            pnt = Point(lat, lon, srid=4326)
            fireblocks = FireBlock.objects.filter(geom__contains=pnt)
            serialized_fireblocks = FireBlockSerializer(fireblocks, many=True) # return the serialized firblock objects
            return Response(serialized_fireblocks.data) #returns to client
        else:
            return Response(FireBlockSerializer(FireBlock.objects.all(),many=True).data) # if no keys, returns unfiltered list of incidents

class FireBlockIncidentsFilterViewSet(generics.ListAPIView):

    queryset = FireBlock.objects.all
    serializer_class = FireBlockSerializer

    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat', ' '))
        lon = float(request.GET.get('lon', ' '))
        start_date = request.GET.get('start_date', ' ')
        end_date = request.GET.get('end_date', ' ')
        fireblocks = FireBlock.objects.all

        if lat != ' ' and lon != ' ':
            pnt = Point(lat, lon, srid=4326)
            fireblocks = FireBlock.objects.filter(geom__contains=pnt)
            fireblockNumber = fireblocks[0].resp_zone
            incidents = Incident.objects.filter(fireblock=fireblockNumber)
            serialized_incidents = IncidentSerializer(incidents, many=True)
            if start_date != ' ' and end_date != ' ':
                incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fireblock=fireblockNumber)
            else:
                incidents = Incident.objects.filter(fireblock=fireblockNumber)
            serialized_incidents = IncidentSerializer(incidents, many=True)
            return Response(serialized_incidents.data)
        else:
            return Response(serialized_incidents.data)

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

class IncidentListViewSet(generics.ListAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys() #get the keys from url
        filter_dict = {}  #create empty dictonary to hold values
        if(k): # checks if keys exist
            for key, value in request.GET.items(): # loops through all keys
                filter_dict[key] = value # adds the values =  filter type of object
            incidents = Incident.objects.filter(**filter_dict) #returns the incidents filtered by selection
            serialized_incidents = IncidentSerializer(incidents, many=True) # return the serialized incident objects
            return Response(serialized_incidents.data) #returns to client
        else:
            return Response(IncidentSerializer(Incident.objects.all(),many=True).data) # if no keys, returns unfiltered list of incidents

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

class FMAListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FMA.objects.all()
    serializer_class = FMASerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys() #get the keys from url
        filter_dict = {}  #create empty dictonary to hold values
        if(k): # checks if keys exist
            for key, value in request.GET.items(): # loops through all keys
                filter_dict[key] = value # adds the values =  filter type of object
            fmas = FMA.objects.filter(**filter_dict) #returns the fmas filtered by selection
            serialized_fmas = FMASerializer(fmas, many=True) # return the serialized fmas objects
            return Response(serialized_fmas.data) #returns to client
        else:
            return Response(FMASerializer(FMA.objects.all(),many=True).data) # if no keys, returns unfiltered list of fmas

class FMAGeoFilterViewSet(generics.ListAPIView):

    queryset = FMA.objects.all
    serializer_class = FMASerializer

    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat', ' '))
        lon = float(request.GET.get('lon', ' '))
        fmas = FMA.objects.all
        if lat != ' ' and lon != ' ':
            pnt = Point(lat, lon, srid=4326)
            fmas = FMA.objects.filter(geom__contains=pnt)
            serialized_fmas = FMASerializer(fmas, many=True) # return the serialized fma objects
            return Response(serialized_fmas.data) #returns to client
        else:
            return Response(FMASerializer(FMA.objects.all(),many=True).data) # if no keys, returns unfiltered list of fmas

class FMAIncidentsFilterViewSet(generics.ListAPIView):

    queryset = FMA.objects.all
    serializer_class = FMASerializer

    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat', ' '))
        lon = float(request.GET.get('lon', ' '))
        start_date = request.GET.get('start_date', ' ')
        end_date = request.GET.get('end_date', ' ')
        fmas = FMA.objects.all

        if lat != ' ' and lon != ' ':
            pnt = Point(lat, lon, srid=4326)
            fmas = FMA.objects.filter(geom__contains=pnt)
            fmaNumber = fmas[0].fma
            incidents = Incident.objects.filter(fmarespcomp=fmaNumber)
            if start_date != ' ' and end_date != ' ':
                incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fmarespcomp=fmaNumber)
            serialized_incidents = IncidentSerializer(incidents, many=True)
            return Response(serialized_incidents.data)
        else:
            return Response(serialized_incidents.data)

class TimeDescViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = TimeDesc.objects.all()
    serializer_class = TimeDescSerializer
