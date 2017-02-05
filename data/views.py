from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import Incident, Agency, AlarmLevel, CensusTract, FireBlock, TypeNatureCode, Station
from data.serializers import IncidentSerializer, AgencySerializer, AlarmLevelSerializer, CensusTractSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def incident_list(request, format=None):

    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        incidents = Incident.objects.all()
        result_page = paginator.paginate_queryset(incidents, request)
        serializedIncidents = IncidentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializedIncidents.data)


@api_view(['GET'])
def agency_list(request, format=None):

    if request.method == 'GET':
        agencies = Agency.objects.all()
        serializedAgencies = AgencySerializer(agencies, many=True)
        return Response(serializedAgencies.data)

@api_view(['GET'])
def alarmlevel_list(request, format=None):

    if request.method == 'GET':
        alarmLevels = AlarmLevel.objects.all()
        serializedAlarmLevel = AlarmLevelSerializer(alarmLevels, many=True)
        return Response(serializedAlarmLevel.data)

@api_view(['GET'])
def censustract_list(request, format=None):

    if request.method == 'GET':
        censusTracts = CensusTract.objects.all()
        serializedCensusTracts = CensusTractSerializer(censusTracts, many=True)
        return Response(serializedCensusTracts.data)

@api_view(['GET'])
def fireblock_list(request, format=None):

    if request.method == 'GET':
        fireBlocks = FireBlock.objects.all()
        serializedFireBlocks = FireBlockSerializer(fireBlocks, many=True)
        return Response(serializedFireBlocks.data)

@api_view(['GET'])
def typenaturecode_list(request, format=None):

    if request.method == 'GET':
        typeNatureCodes = TypeNatureCode.objects.all()
        serializedTypeNatureCodes = TypeNatureCodeSerializer(typeNatureCodes, many=True)
        return Response(serializedTypeNatureCodes.data)

@api_view(['GET'])
def station_list(request, format=None):

    if request.method == 'GET':
        stations = Station.objects.all()
        serializedStations = StationSerializer(stations, many=True)
        return Response(serializedStations.data)
