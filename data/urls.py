"""emergency_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from data import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Emergency Response API')

urlpatterns = [

    url(r'^agencies/$', views.AgencyListViewSet.as_view(), name='agencies'),
    url(r'^agencies/(?P<pk>[0-9]+)/$', views.AgencyRetrieveViewSet.as_view(), name='agencies'),

    url(r'^alarmlevels/$', views.AlarmLevelListViewSet.as_view(), name='alarmlevels'),

    url(r'^fireblocks/$', views.FireBlockListViewSet.as_view(), name='fireblocks'),
    url(r'^fireblock/$', views.FireBlockGeoFilterViewSet.as_view(), name='fireblock'),
    url(r'^fireblock/incidents/$', views.FireBlockIncidentsFilterViewSet.as_view(), name='fireblock/incidents'),

    url(r'^fmas/$', views.FMAListViewSet),
    url(r'^fmas/(?P<pk>[0-9]+)/$', views.FMARetrieveViewSet.as_view(), name='fmas'),
    url(r'^fma/$', views.FMAGeoFilterViewSet.as_view(), name='fma'),
    url(r'^fma/incidents/$', views.FMAIncidentsFilterViewSet.as_view(), name='fma/incidents'),

    # url(r'^geocoder/$', views.address_geocode, name='geocoder'),

    url(r'^incidents/$', views.IncidentListViewSet.as_view(), name='incidents'),
    url(r'^incidents/info/$', views.IncidentInfoViewSet.as_view(), name='incidents'),
    url(r'^incidents/foundclass/$', views.IncsitFoundClassListViewSet.as_view(), name='incidents'),
    url(r'^incidents/foundclass_sub/$', views.IncsitFoundSubListViewSet.as_view(), name='incidents'),
    url(r'^incidents/found/$', views.IncsitFoundListViewSet.as_view(), name='incidents'),
    url(r'^incidents/times/$', views.IncidentTimesListViewSet.as_view(), name='incidents'),
    url(r'^incidents/times/(?P<pk>[0-9]+)/$', views.IncidentTimesRetrieveViewSet.as_view(), name='incidents'),

    url(r'^mutualaid/$', views.MutualAidListViewSet.as_view(), name='mutualaid'),
    url(r'^mutualaid/(?P<pk>[0-9]+)/$', views.MutualAidRetrieveViewSet.as_view(), name='mutualaid'),

    url(r'^responders/$', views.ResponderListViewSet.as_view(), name='responders'),
    url(r'^responders/(?P<pk>[0-9]+)/$', views.ResponderRetrieveViewSet.as_view(), name='responders'),

    url(r'^responderunits/$', views.ResponderUnitListViewSet.as_view(), name='responderunits'),
    url(r'^responderunits/(?P<pk>[0-9]+)/$', views.ResponderUnitRetrieveViewSet.as_view(), name='responderunits'),

    url(r'^stations/$', views.StationListViewSet.as_view(), name='stations'),
    url(r'^stations/(?P<pk>[0-9]+)/$', views.StationRetrieveViewSet.as_view(), name='stations'),

    url(r'^situationfound/$', views.SituationFoundListViewSet.as_view(), name='situationfound'),
    url(r'^situationfound/(?P<pk>[0-9]+)/$', views.SituationFoundRetrieveViewSet.as_view(), name='situationfound'),

    url(r'^timedescriptions/$', views.TimeDescListViewSet.as_view(), name='timedescriptions'),
    url(r'^timedescriptions/(?P<pk>[0-9]+)/$', views.TimeDescRetrieveViewSet.as_view(), name='timedescriptions'),

    url(r'^typenaturecodes/$', views.TypeNatureCodeListViewSet.as_view(), name='typenaturecodes'),
    url(r'^typenaturecodes/(?P<pk>[0-9]+)/$', views.TypeNatureCodeRetrieveViewSet.as_view(), name='typenaturecodes'),

    url(r'^$', schema_view)
]

urlpatterns += staticfiles_urlpatterns()
