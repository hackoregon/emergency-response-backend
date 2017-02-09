from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import Agency, AlarmLevel, CensusTract, FireBlock, TypeNatureCode, Station, FireStation, FMA, MutualAid, ResponderUnit, IncsitFoundClass, IncsitFoundSub, IncsitFound, Incident, FireBlock
from data.serializers import AgencySerializer, AlarmLevelSerializer, CensusTractSerializer, FireBlockSerializer, TypeNatureCodeSerializer, StationSerializer, FireStationSerializer, FMASerializer, MutualAidSerializer, ResponderUnitSerializer, IncsitFoundClassSerializer, IncsitFoundSubSerializer, IncsitFoundSerializer, IncidentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AlarmLevelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = AlarmLevel.objects.all()
    serializer_class = AlarmLevelSerializer

class CensusTractViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = CensusTract.objects.all()
    serializer_class = CensusTractSerializer

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

class FireStationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FireStation.objects.all()
    serializer_class = FireStationSerializer

class FMAViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide 'list' and 'detail' actions.
    """

    queryset = FMA.objects.all()
    serializer_class = FMASerializer

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

# @api_view(['GET'])
# def incident_list(request, format=None):
#
#     if request.method == 'GET':
#         paginator = PageNumberPagination()
#         paginator.page_size = 10
#         incidents = Incident.objects.all()
#         result_page = paginator.paginate_queryset(incidents, request)
#         serializedIncidents = IncidentSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializedIncidents.data)
