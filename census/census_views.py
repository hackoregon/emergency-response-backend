from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from django.contrib.gis.geos import Point
from census.models import CensusBlock, CensusEducationalAttainment
from census.serializers import CensusBlockSerializer, CensusEducationalAttainmentSerializer

class CensusBlockListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusBlock.objects.all()
    serializer_class = CensusBlockSerializer

class CensusBlockRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusBlock.objects.all()
    serializer_class = CensusBlockSerializer

class CensusEducationalAttainmentListViewSet(generics.ListAPIView):
    """
    This viewset will provide 'list' action.
    """

    queryset = CensusEducationalAttainment.objects.all()
    serializer_class = CensusEducationalAttainmentSerializer

class CensusEducationalAttainmentRetrieveViewSet(generics.RetrieveAPIView):
    """
    This viewset will provide the 'detail' action.
    """

    queryset = CensusEducationalAttainment.objects.all()
    serializer_class = CensusEducationalAttainmentSerializer
