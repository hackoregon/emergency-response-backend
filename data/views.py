from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
import django_filters
import coreapi
from django.contrib.gis.geos import Point
from django.db.models import Avg, Max
from django.db import connection
from data.models import Agency, AlarmLevel, FireBlock, TypeNatureCode, Station, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FireBlock, FMA, TimeDesc, Responder, IncidentTimes, SituationFound, FMAStats

from data.serializers import AgencySerializer, AlarmLevelSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer, MutualAidSerializer, ResponderUnitSerializer, IncsitFoundClassSerializer, IncsitFoundSubSerializer, IncsitFoundSerializer, IncidentSerializer, FMASerializer, TimeDescSerializer, ResponderSerializer, IncidentTimesSerializer, SituationFoundSerializer, IncidentIncidentTimesSerializer, IncidentResponderSerializer, FMAStatsSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Pagination filters to be called on endpoints depending on the size of the data set.
# ie: add     pagination_class = StandardResultsSetPagination to the desired viewset.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 1000

# add AddressGeocode and AddressGeocodeSerializer to models and serializers imports if using geocoder (maybe refactor/update if changed)

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


## Viewsets for Fireblocks

class FireBlockListViewSet(generics.ListAPIView):
    """
    This viewset will provide a list of Fireblocks.
    """

    queryset = FireBlock.objects.all()
    serializer_class = FireBlockSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'gid': ['exact',],
            'fma': ['exact',],
            }

## This filter is necessary to add query params into swagger(open issue at this time: https://github.com/marcgibbons/django-rest-swagger/issues/549)

class LatLonGeoFilter(GeoFilterSet):

    class Meta:
        model = FireBlock
        fields = []

    # this function adds the params to the Swagger UI
    def get_schema_fields(self, view):
        fields = []
        lat = coreapi.Field(
            name="lat",
            location="query",
            description="Latitude of search point",
            type="number",
            )
        lon = coreapi.Field(
            name="lon",
            location="query",
            description="Longitude of search point",
            type="number",
            )
        gid = coreapi.Field(
            name="gid",
            location="query",
            description="Fireblock id",
            type="number",
            )
        fields.append(lat)
        fields.append(lon)
        fields.append(gid)
        return fields

# Filters fireblocks by their gid (primary_key) or containing a Lat/Lon

class FireBlockGeoFilterViewSet(generics.ListAPIView):
    """
    This endpoint filters for a fireblock based on the latitude and longitude combination or the fireblock's gid.
    It will return a list with a single fireblock's information and geom.
    """

    queryset = FireBlock.objects.all
    serializer_class = FireBlockSerializer
    # Include the filter
    filter_backends = (LatLonGeoFilter,)

    def get(self, request, *args, **kwargs):
        if request.GET.get('gid', ' ') == ' ':
            if request.GET.get('lat', ' ') != ' ' and request.GET.get('lon', ' ') != ' ':
                try:
                    lat = float(request.GET.get('lat', ' '))
                    lon = float(request.GET.get('lon', ' '))
                    pnt = Point(lon, lat, srid=4326)
                    fireblocks = FireBlock.objects.filter(geom__contains=pnt)
                    if fireblocks:
                        serialized_fireblocks = FireBlockSerializer(fireblocks, many=True) # return the serialized fireblock objects
                        return Response(serialized_fireblocks.data) #returns to client
                    else:
                        return Response('No Fireblock found for this latitude and longitude.', status=status.HTTP_404_NOT_FOUND)
                except ValueError:
                    return Response('Latitude or longitude is invalid.', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Missing either gid or latitude and longitude paramaters.', status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                gid = float(request.GET.get('gid', ' '))
                fireblocks = [FireBlock.objects.get(gid=gid)]
                if fireblocks:
                    serialized_fireblocks = FireBlockSerializer(fireblocks, many=True) # return the serialized fireblock objects
                    return Response(serialized_fireblocks.data) #returns to client
                else:
                    return Response('No Fireblock found for this gid.', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Gid is invalid.', status=status.HTTP_400_BAD_REQUEST)

# This function adds start and end date to the Fireblock filter
class DateFilter(DjangoFilterBackend):

    class Meta:
        model = FireBlock
        fields = []
    # Function to add query params to Swagger UI
    def get_schema_fields(self, view):
        fields = []
        start_date = coreapi.Field(
            name="start_date",
            location="query",
            description="YYYY-MM-DD",
            type="datetime",
            )
        end_date = coreapi.Field(
            name="end_date",
            location="query",
            description="YYYY-MM-DD",
            type="datetime",
            )
        fields.append(start_date)
        fields.append(end_date)
        return fields

# This endpoint returns information about incidents in the Fireblock.

class FireBlockIncidentsFilterViewSet(generics.ListAPIView):
    """
    This endpoint filters for incidents within a specific fireblock.
    It filters based on geolocation, as well as date range.
    Results are paginated at 50 with max_page_size of 100.
    """

    queryset = FireBlock.objects.all
    serializer_class = FireBlockSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (LatLonGeoFilter, DateFilter)

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date', ' ')
        end_date = request.GET.get('end_date', ' ')
        if request.GET.get('gid', ' ') == ' ':
            if request.GET.get('lat', ' ') != ' ' and request.GET.get('lon', ' ') != ' ':
                try:
                    lat = float(request.GET.get('lat', ' '))
                    lon = float(request.GET.get('lon', ' '))
                    pnt = Point(lon, lat, srid=4326)
                    fireblocks = FireBlock.objects.filter(geom__contains=pnt)
                    if fireblocks:
                        fireblockNumber = fireblocks[0].resp_zone
                        if start_date != ' ' and end_date != ' ':
                            incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fireblock=fireblockNumber)
                        else:
                            incidents = Incident.objects.filter(fireblock=fireblockNumber)
                        if incidents:
                            serialized_incidents = IncidentSerializer(incidents, many=True)
                            return Response(serialized_incidents.data)
                        else:
                            return Response('No Incidents found for the fireblock in this date range.', status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response('No Fireblock found for this latitude and longitude.', status=status.HTTP_404_NOT_FOUND)
                except ValueError:
                    return Response('Latitude or longitude is invalid.', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Missing either gid or latitude and longitude paramaters.', status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                gid = float(request.GET.get('gid', ' '))
                fireblocks = [FireBlock.objects.get(gid=gid)]
                if fireblocks:
                    fireblockNumber = fireblocks[0].resp_zone
                    if start_date != ' ' and end_date != ' ':
                        incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fireblock=fireblockNumber)
                    else:
                        incidents = Incident.objects.filter(fireblock=fireblockNumber)
                    if incidents:
                        serialized_incidents = IncidentSerializer(incidents, many=True)
                        return Response(serialized_incidents.data)
                    else:
                        return Response('No Incidents found for the fireblock in this date range.', status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response('No Fireblock found for this gid.', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Gid is invalid.', status=status.HTTP_400_BAD_REQUEST)
## These are the viewsets based on FMAs

class FMAListViewSet(generics.ListAPIView):
    """
    This endpoint provides the fma id and geoms for all FMAs (Fire Management Areas).
    """

    queryset = FMA.objects.all()
    serializer_class = FMASerializer

class FMALatLonGeoFilter(GeoFilterSet):

    class Meta:
        model = FMA
        fields = []

    def get_schema_fields(self, view):
        fields = []
        lat = coreapi.Field(
            name="lat",
            location="query",
            description="Latitude of search point",
            type="number",
            )
        lon = coreapi.Field(
            name="lon",
            location="query",
            description="Longitude of search point",
            type="number",
            )
        fma_id = coreapi.Field(
            name="fma_id",
            location="query",
            description="FMA id",
            type="number",
            )
        fields.append(lat)
        fields.append(lon)
        fields.append(fma_id)
        return fields

class FMADateFilter(DjangoFilterBackend):

    class Meta:
        model = FMA
        fields = []

    def get_schema_fields(self, view):
        fields = []
        start_date = coreapi.Field(
            name="start_date",
            location="query",
            description="YYYY-MM-DD",
            type="datetime",
            )
        end_date = coreapi.Field(
            name="end_date",
            location="query",
            description="YYYY-MM-DD",
            type="datetime",
            )
        # totals = coreapi.Field(
        #     name="totals",
        #     location="query",
        #     description="True to return only total number",
        #     type="boolean",
        #     )
        fields.append(start_date)
        fields.append(end_date)
        # fields.append(totals)

        return fields

class FMAGeoFilterViewSet(generics.ListAPIView):
    """
    This endpoint finds an FMA based on a latitude and longitude. It returns an id, the geom, and demographic stats about a FMA.
    
    Explanation of Demographic Data:
        fma = id of the FMA
        fma_population_total = total population in the FMA
        percent_owner_occ_hh = percentage of households in FMA occupied by owner
        percent_renter_occ_hh = percentage of households in FMA occupied by a renter
        median_hh_income = median household income for FMA
        percent_w_hinsurance = percentage of population with health insurance
        percent_wo_hinsurance = percentage of population without health insurance
        percent_college_grad_or_higher = percentage of population that has graduated college or higher
        percent_rec_fs = percentage of population that receives foodstamps
        percent_total_lesh = limeted english speakings households
        percent_non_white = models.FloatField(blank=True, null=True)
        percent_below_pov = models.FloatField(blank=True, null=True)
        percent_member_65plus = models.FloatField(blank=True, null=True)
        percent_diff_area = models.FloatField(blank=True, null=True)
        median_response_time = models.FloatField(blank=True, null=True)
        ave_weekly_incidents = models.FloatField(blank=True, null=True)
    """

    queryset = FMA.objects.all
    serializer_class = FMASerializer
    filter_backends = (FMALatLonGeoFilter,)

    def get(self, request, *args, **kwargs):
        if request.GET.get('fma_id', ' ') == ' ':
            if request.GET.get('lat', ' ') != ' ' and request.GET.get('lon', ' ') != ' ':
                try:
                    lat = float(request.GET.get('lat', ' '))
                    lon = float(request.GET.get('lon', ' '))
                    pnt = Point(lon, lat, srid=4326)
                    fmas = FMA.objects.filter(geom__contains=pnt)
                    if fmas:
                        fma_id = fmas[0].fma
                        fma_stats = FMAStats.objects.get(fma=fma_id)
                        serialized_fmas = FMASerializer(fmas, many=True) # return the serialized fma objects
                        serialized_stats = FMAStatsSerializer(fma_stats)
                        return Response({
                            'id': fma_id,
                            'geometry': serialized_fmas.data,
                            'stats': serialized_stats.data,
                                })
                    else:
                        return Response('No FMA found for this latitude and longitude.', status=status.HTTP_404_NOT_FOUND)
                except ValueError:
                    return Response('Latitude or longitude is invalid.', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Missing latitude or longitude paramater.', status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                fma_id = int(request.GET.get('fma_id', ' '))
                fmas = [FMA.objects.get(fma=fma_id)]
                if fmas:
                    fma_id = fmas[0].fma
                    fma_stats = FMAStats.objects.get(fma=fma_id)
                    serialized_fmas = FMASerializer(fmas, many=True) # return the serialized fma objects
                    serialized_stats = FMAStatsSerializer(fma_stats)
                    return Response({
                        'id': fma_id,
                        'geometry': serialized_fmas.data,
                        'stats': serialized_stats.data,
                            })
                else:
                    return Response('No FMA found for this FMA.', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('FMA is invalid.', status=status.HTTP_400_BAD_REQUEST)

class FMAIncidentsFilterViewSet(generics.ListAPIView):
    """
    This view returns all incidents for a FMA based on a latitude and longitude.
    It can be further filtered by a date range.
    If passed param totals = True will return only the total number of incidents.
    Otherwise will return the total number and individual incidents.
    """

    queryset = FMA.objects.all
    serializer_class = FMASerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (FMALatLonGeoFilter, FMADateFilter,)


    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date', ' ')
        end_date = request.GET.get('end_date', ' ')
        totals = request.GET.get('totals', ' ')
        if request.GET.get('fma_id', ' ') == ' ':
            if request.GET.get('lat') and request.GET.get('lon'):
                try:
                    lat = float(request.GET.get('lat', ' '))
                    lon = float(request.GET.get('lon', ' '))
                    pnt = Point(lon, lat, srid=4326)
                    fmas = FMA.objects.filter(geom__contains=pnt)
                    fmaNumber = fmas[0].fma
                    if start_date != ' ' and end_date != ' ':
                        incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fmarespcomp=fmaNumber)
                    else:
                        incidents = Incident.objects.filter(fmarespcomp=fmaNumber)
                    serialized_incidents = IncidentSerializer(incidents, many=True)
                    total_incidents = incidents.count()

                    return Response({
                        "incidents": serialized_incidents.data,
                        "total_incidents": total_incidents})
                except ValueError:
                    return Response('Lat and Lon values must be postive or negative float values', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Missing either fma_id or Lat and Lon parameters', status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                fma_id = int(request.GET.get('fma_id', ' '))
                fmas = [FMA.objects.get(fma=fma_id)]
                if fmas:
                    if start_date != ' ' and end_date != ' ':
                        fmaNumber = fmas[0].fma
                        incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fmarespcomp=fmaNumber)
                    else:
                        fmaNumber = fmas[0].fma
                        incidents = Incident.objects.filter(incdate__range=(start_date, end_date), fmarespcomp=fmaNumber)
                    serialized_incidents = IncidentSerializer(incidents, many=True)
                    total_incidents = incidents.count()
                    return Response({
                        "incidents": serialized_incidents.data,
                        "total_incidents": total_incidents})
                else:
                    return Response('FMA not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('FMA_ID is invalid.', status=status.HTTP_400_BAD_REQUEST)
class FMARetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = FMA.objects.all()
    serializer_class = FMASerializer

## These are the viewsets for Incidents

class IncidentListViewSet(generics.ListAPIView):
    """
    This viewset will provide the 'list' action.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    pagination_class = StandardResultsSetPagination

class IncidentInfoViewSet(generics.ListAPIView):
    """
    This viewset will provide the details of an incident, returning the incident model, related incident_times, and responder units. It will also return a calculated response_time for the incident
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filter_fields = ("incident_id",)
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
                return Response('Incident ID must be integer', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Missing Incident ID paramater', status=status.HTTP_400_BAD_REQUEST)


### These are the viewsets that have not needed custom filtering

class AgencyListViewSet(generics.ListAPIView):
    """
    This viewset lists the agencies that respond to emergency incidents within Portland.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'description': ['icontains'],
        'statecode': ['icontains']
    }


class AgencyRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset retrievies a specific agency.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AlarmLevelListViewSet(generics.ListAPIView):
    """
    This viewset lists the levels of alarms.
    """

    queryset = AlarmLevel.objects.all()
    serializer_class = AlarmLevelSerializer

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

#### These viewsets are not being used at this time:
