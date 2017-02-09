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

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agencies', views.AgencyViewSet)
router.register(r'alarmlevels', views.AlarmLevelViewSet)
router.register(r'censustracts', views.CensusTractViewSet)
router.register(r'fireblocks', views.FireBlockViewSet)
router.register(r'typenaturecodes', views.TypeNatureCodeViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'firestations', views.FireStationViewSet)
router.register(r'fmas', views.FMAViewSet)
router.register(r'mutualaid', views.MutualAidViewSet)
router.register(r'responderunits', views.ResponderUnitViewSet)
router.register(r'incsitfoundclass', views.IncsitFoundClassViewSet)
router.register(r'incsitfoundsub', views.IncsitFoundSubViewSet)
router.register(r'incsitfound', views.IncsitFoundViewSet)
router.register(r'incidents', views.IncidentViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
