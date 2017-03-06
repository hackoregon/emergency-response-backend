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
from rest_framework_swagger.views import get_swagger_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_swagger_view(title='Emergency Response API')
# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'agencies', views.AgencyViewSet)
# router.register(r'alarmlevels', views.AlarmLevelViewSet)
# router.register(r'fireblocks', views.FireBlockViewSet)
# router.register(r'typenaturecodes', views.TypeNatureCodeViewSet)
# router.register(r'stations', views.StationViewSet)
# router.register(r'mutualaid', views.MutualAidViewSet)
# router.register(r'responderunits', views.ResponderUnitViewSet)
# router.register(r'incsitfoundclass', views.IncsitFoundClassViewSet)
# router.register(r'incsitfoundsub', views.IncsitFoundSubViewSet)
# router.register(r'incsitfound', views.IncsitFoundViewSet)
# router.register(r'incidents', views.IncidentViewSet)
# router.register(r'census/blocks', views.CensusBlockViewSet)
# router.register(r'census/householdincomes', views.CensusHouseholdIncomeViewSet)
# router.register(r'census/householdlanguages', views.CensusHouseholdLanguageViewSet)
# router.register(r'census/household65plus', views.CensusHousehold65PlusViewSet)
# router.register(r'census/housingtenure', views.CensusHousingTenureViewSet)
# router.register(r'census/medianhouseholdincome', views.CensusMedianHouseholdIncomeViewSet)
# router.register(r'census/race', views.CensusRaceViewSet)
# router.register(r'census/totalpopulation', views.CensusTotalPopulationViewSet)
# # router.register(r'fcbproportion', views.FcbProportionViewSet)
# # router.register(r'fmashapes', views.FmaShapeViewSet)
# router.register(r'timedescription', views.TimeDescViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agencies/$', views.AgencyViewSet.as_view({'get': 'list'}), name='agencies'),
    url(r'^agencies/(?P<pk>[0-9]+)/$', views.AgencyViewSet.as_view({'get': 'retrieve'}), name='agencies'),
    url(r'^alarmlevels/$', views.AlarmLevelViewSet.as_view({'get': 'list'}), name='alarmlevels'),
    url(r'^alarmlevels/(?P<pk>[0-9]+)/$', views.AlarmLevelViewSet.as_view({'get': 'retrieve'}), name='alarmlevels'),
    url(r'^incidents/$', views.IncidentListViewSet.as_view(), name='incidents'),
    url(r'^incidents/(?P<pk>[0-9]+)/$', views.IncidentViewSet.as_view({'get': 'retrieve'}), name='incidents'),
    url(r'^fireblocks/$', views.FireBlockListViewSet.as_view(), name='fireblocks'),
    url(r'^fireblock/$', views.FireBlockGeoFilterViewSet.as_view(), name='fireblock'),
    url(r'^fireblock/incidents/$', views.FireBlockIncidentsFilterViewSet.as_view(), name='fireblock/incidents'),
    url(r'^fmas/$', views.FMAListViewSet.as_view(), name='fmas'),
    url(r'^fma/$', views.FMAGeoFilterViewSet.as_view(), name='fma'),
    url(r'^fma/incidents/$', views.FMAIncidentsFilterViewSet.as_view(), name='fma/incidents'),
    url(r'^$', schema_view)
]

urlpatterns += staticfiles_urlpatterns()
