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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agencies/$', views.AgencyListViewSet.as_view(), name='agencies'),
    url(r'^agencies/(?P<pk>[0-9]+)/$', views.AgencyRetrieveViewSet.as_view(), name='agencies'),
    url(r'^alarmlevels/$', views.AlarmLevelListViewSet.as_view(), name='alarmlevels'),
    url(r'^alarmlevels/(?P<pk>[0-9]+)/$', views.AlarmLevelRetrieveViewSet.as_view(), name='alarmlevels'),
    url(r'^incidents/$', views.IncidentListViewSet.as_view(), name='incidents'),
    url(r'^incidents/(?P<pk>[0-9]+)/$', views.IncidentRetrieveViewSet.as_view(), name='incidents'),
    url(r'^incidents/totals/$', views.IncidentCountViewSet.as_view(), name='incidents/totals'),
    url(r'^fireblocks/$', views.FireBlockListViewSet.as_view(), name='fireblocks'),
    url(r'^fireblocks/(?P<pk>[0-9]+)/$', views.FireBlockRetrieveViewSet.as_view(), name='fireblocks'),
    url(r'^fireblock/$', views.FireBlockGeoFilterViewSet.as_view(), name='fireblock'),
    url(r'^fireblock/incidents/$', views.FireBlockIncidentsFilterViewSet.as_view(), name='fireblock/incidents'),
    url(r'^fmas/$', views.FMAListViewSet.as_view(), name='fmas'),
    url(r'^fma/$', views.FMAGeoFilterViewSet.as_view(), name='fma'),
    url(r'^fma/incidents/$', views.FMAIncidentsFilterViewSet.as_view(), name='fma/incidents'),
    url(r'^$', schema_view)
]

urlpatterns += staticfiles_urlpatterns()
