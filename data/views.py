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
from data.models import Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FireBlock, FcbProportion, FMA, TimeDesc, Responder, IncidentTimes, SituationFound

from data.serializers import AgencySerializer, AlarmLevelSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer, MutualAidSerializer, ResponderUnitSerializer, IncsitFoundClassSerializer, IncsitFoundSubSerializer, IncsitFoundSerializer, IncidentSerializer, FcbProportionSerializer, FMASerializer, TimeDescSerializer, ResponderSerializer, IncidentTimesSerializer, SituationFoundSerializer, IncidentIncidentTimesSerializer, IncidentResponderSerializer
from django_filters.rest_framework import DjangoFilterBackend

# add AddressGeocode and AddressGeocodeSerializer to models and serializers imports if using geocoder

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

# @api_view(['GET'])
# def address_geocode(request, format=None, *args, **kwargs):
#     """
#     This viewset will provide 'list' action for a geocode response to an address.
#     """
#     if request.method == 'GET':
#         address = request.GET.get('address', ' ')
#
#         addresses = AddressGeocode.objects.using('geocoder').raw("SELECT g.rating, ST_X(g.geomout) As lon, ST_Y(g.geomout) As lat, (addy).address As stno, (addy).streetname As street, (addy).streettypeabbrev As styp, (addy).location As city, (addy).stateabbrev As st,(addy).zip FROM geocode(%s) As g;", [address])
#
#         serializedAddresses = AddressGeocodeSerializer(addresses, many=True)
#         return Response(serializedAddresses.data)

class AgencyListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'description': ['exact', 'icontains'],
        'statecode': ['exact', 'icontains']
    }

class AgencyRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AlarmLevelListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = AlarmLevel.objects.all()
    serializer_class = AlarmLevelSerializer

class AlarmLevelRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'detail' action.
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
            pnt = Point(lon, lat, srid=4326)
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
            pnt = Point(lon, lat, srid=4326)
            fireblocks = FireBlock.objects.filter(geom__contains=pnt)
            fireblockNumber = fireblocks[0].resp_zone
            if start_date != ' ' and end_date != ' ':
                incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fireblock=fireblockNumber)
            else:
                incidents = Incident.objects.filter(fireblock=fireblockNumber)
            serialized_incidents = IncidentSerializer(incidents, many=True)
            return Response(serialized_incidents.data)
        else:
            return Response(serialized_incidents.data)

class FireBlockRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = FireBlock.objects.all()
    serializer_class = FireBlockSerializer

class TypeNatureCodeListViewSet(generics.ListAPIView):
    """
    This viewset will provide the 'list' action.
    """

    queryset = TypeNatureCode.objects.all()
    serializer_class = TypeNatureCodeSerializer

class TypeNatureCodeRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = TypeNatureCode.objects.all()
    serializer_class = TypeNatureCodeSerializer

class StationListViewSet(generics.ListAPIView):
    """
    This viewset will provide the 'list' action.
    """

    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = Station.objects.all()
    serializer_class = StationSerializer

class MutualAidListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = MutualAid.objects.all()
    serializer_class = MutualAidSerializer

class MutualAidRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = MutualAid.objects.all()
    serializer_class = MutualAidSerializer

class ResponderUnitListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = ResponderUnit.objects.all()
    serializer_class = ResponderUnitSerializer

class ResponderUnitRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'detail' action.
    """

    queryset = ResponderUnit.objects.all()
    serializer_class = ResponderUnitSerializer

class IncsitFoundClassListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = IncsitFoundClass.objects.all()
    serializer_class = IncsitFoundClassSerializer

class IncsitFoundClassRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'detail' action.
    """

    queryset = IncsitFoundClass.objects.all()
    serializer_class = IncsitFoundClassSerializer

class IncsitFoundSubListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = IncsitFoundSub.objects.all()
    serializer_class = IncsitFoundSubSerializer

class IncsitFoundSubRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'detail' action.
    """

    queryset = IncsitFoundSub.objects.all()
    serializer_class = IncsitFoundSubSerializer

class IncsitFoundListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = IncsitFound.objects.all()
    serializer_class = IncsitFoundSerializer

class IncsitFoundRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide 'detail' action.
    """

    queryset = IncsitFound.objects.all()
    serializer_class = IncsitFoundSerializer


class IncidentListViewSet(generics.ListAPIView):
    """
    This viewset will provide the 'list' action.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    pagination_class = StandardResultsSetPagination

class IncidentInfoViewSet(generics.ListAPIView):
    """
    This viewset will provide the details of an incident.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def get(self, request, *args, **kwargs):
        if request.GET.get('incident_id', ' ') != ' ':
            this_incident_id = request.GET.get('incident_id', ' ')
            try:
                incidents = Incident.objects.filter(incident_id=this_incident_id)
                if incidents:
                    serialized_incidents = IncidentSerializer(incidents, many=True)
                    incident_times = IncidentTimes.objects.filter(incident_id=this_incident_id).order_by("realtime")
                    serialized_itimes = IncidentIncidentTimesSerializer(incident_times, many=True)
                    first_response=incident_times.get(timedesc=0)
                    on_scene=incident_times.filter(timedesc=5).order_by("realtime")
                    first_on_scene=on_scene[0]
                    response_time=(first_on_scene.realtime-first_response.realtime).total_seconds()
                    responders = Responder.objects.filter(incident_id=this_incident_id)
                    serialized_responders = IncidentResponderSerializer(responders, many=True)
                    return Response({
                        'data': serialized_incidents.data,
                        'incident_times': serialized_itimes.data,
                        'responders':serialized_responders.data,
                        'response_time':response_time
                            })
                else:
                    return Response('Incident ID not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Incident ID must be integer', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Missing Incident ID paramater', status=status.HTTP_400_BAD_REQUEST)

class IncidentTimesListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = IncidentTimes.objects.all()
    serializer_class = IncidentTimesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'incident_id': ['exact',],
        }

class IncidentTimesRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = IncidentTimes.objects.all()
    serializer_class = IncidentTimesSerializer

class IncidentCountViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class FcbProportionListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = FcbProportion.objects.all()
    serializer_class = FcbProportionSerializer

class FcbProportionListRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
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
            pnt = Point(lon, lat, srid=4326)
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
            pnt = Point(lon, lat, srid=4326)
            fmas = FMA.objects.filter(geom__contains=pnt)
            fmaNumber = fmas[0].fma
            if start_date != ' ' and end_date != ' ':
                incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fmarespcomp=fmaNumber)
            else:
                incidents = Incident.objects.filter(fmarespcomp=fmaNumber)
            serialized_incidents = IncidentSerializer(incidents, many=True)
            return Response(serialized_incidents.data)
        else:
            return Response(serialized_incidents.data)

class FMARetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = FMA.objects.all()
    serializer_class = FMASerializer

class TimeDescListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = TimeDesc.objects.all()
    serializer_class = TimeDescSerializer

class TimeDescRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = TimeDesc.objects.all()
    serializer_class = TimeDescSerializer

class ResponderListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = Responder.objects.all()
    serializer_class = ResponderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'incident_id': ['exact', 'icontains'],
    }

class ResponderRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = Responder.objects.all()
    serializer_class = ResponderSerializer

class SituationFoundListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = SituationFound.objects.all()
    serializer_class = SituationFoundSerializer

class SituationFoundRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = SituationFound.objects.all()
    serializer_class = SituationFoundSerializer
