"""emergency_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^emergency/$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^emergency/$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^emergency/blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from data import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


schema_view = get_schema_view(title='Emergency Response API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^emergency/agencies/$', views.AgencyListViewSet.as_view(), name='agencies'),
    url(r'^emergency/agencies/(?P<pk>[0-9]+)/$', views.AgencyRetrieveViewSet.as_view(), name='agencies'),

    url(r'^emergency/alarmlevels/$', views.AlarmLevelListViewSet.as_view(), name='alarmlevels'),
    url(r'^emergency/alarmlevels/(?P<pk>[0-9]+)/$', views.AlarmLevelRetrieveViewSet.as_view(), name='alarmlevels'),

    url(r'^emergency/fireblocks/$', views.FireBlockListViewSet.as_view(), name='fireblocks'),
    url(r'^emergency/fireblocks/(?P<pk>[0-9]+)/$', views.FireBlockRetrieveViewSet.as_view(), name='fireblocks'),
    url(r'^emergency/fireblock/$', views.FireBlockGeoFilterViewSet.as_view(), name='fireblock'),
    url(r'^emergency/fireblock/incidents/$', views.FireBlockIncidentsFilterViewSet.as_view(), name='fireblock/incidents'),

    url(r'^emergency/fmas/$', views.FMAListViewSet.as_view(), name='fmas'),
    url(r'^emergency/fmas/(?P<pk>[0-9]+)/$', views.FMARetrieveViewSet.as_view(), name='fmas'),
    url(r'^emergency/fma/$', views.FMAGeoFilterViewSet.as_view(), name='fma'),
    url(r'^emergency/fma/incidents/$', views.FMAIncidentsFilterViewSet.as_view(), name='fma/incidents'),

    # url(r'^emergency/geocoder/$', views.address_geocode, name='geocoder'),

    url(r'^emergency/incidents/$', views.IncidentListViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/info/$', views.IncidentInfoViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/totals/$', views.IncidentCountViewSet.as_view(), name='incidents/totals'),
    url(r'^emergency/incidents/foundclass/$', views.IncsitFoundClassListViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/foundclass/(?P<pk>[0-9]+)/$', views.IncsitFoundClassRetrieveViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/foundclass_sub/$', views.IncsitFoundSubListViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/foundclass_sub/(?P<pk>[0-9]+)/$', views.IncsitFoundSubRetrieveViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/found/$', views.IncsitFoundListViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/found/(?P<pk>[0-9]+)/$', views.IncsitFoundRetrieveViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/times/$', views.IncidentTimesListViewSet.as_view(), name='incidents'),
    url(r'^emergency/incidents/times/(?P<pk>[0-9]+)/$', views.IncidentTimesRetrieveViewSet.as_view(), name='incidents'),

    url(r'^emergency/mutualaid/$', views.MutualAidListViewSet.as_view(), name='mutualaid'),
    url(r'^emergency/mutualaid/(?P<pk>[0-9]+)/$', views.MutualAidRetrieveViewSet.as_view(), name='mutualaid'),

    url(r'^emergency/responders/$', views.ResponderListViewSet.as_view(), name='responders'),
    url(r'^emergency/responders/(?P<pk>[0-9]+)/$', views.ResponderRetrieveViewSet.as_view(), name='responders'),

    url(r'^emergency/responderunits/$', views.ResponderUnitListViewSet.as_view(), name='responderunits'),
    url(r'^emergency/responderunits/(?P<pk>[0-9]+)/$', views.ResponderUnitRetrieveViewSet.as_view(), name='responderunits'),

    url(r'^emergency/stations/$', views.StationListViewSet.as_view(), name='stations'),
    url(r'^emergency/stations/(?P<pk>[0-9]+)/$', views.StationRetrieveViewSet.as_view(), name='stations'),

    url(r'^emergency/situationfound/$', views.SituationFoundListViewSet.as_view(), name='situationfound'),
    url(r'^emergency/situationfound/(?P<pk>[0-9]+)/$', views.SituationFoundRetrieveViewSet.as_view(), name='situationfound'),

    url(r'^emergency/timedescriptions/$', views.TimeDescListViewSet.as_view(), name='timedescriptions'),
    url(r'^emergency/timedescriptions/(?P<pk>[0-9]+)/$', views.TimeDescRetrieveViewSet.as_view(), name='timedescriptions'),

    url(r'^emergency/typenaturecodes/$', views.TypeNatureCodeListViewSet.as_view(), name='typenaturecodes'),
    url(r'^emergency/typenaturecodes/(?P<pk>[0-9]+)/$', views.TypeNatureCodeRetrieveViewSet.as_view(), name='typenaturecodes'),

    url(r'^emergency/$', schema_view)
]

urlpatterns += staticfiles_urlpatterns()
