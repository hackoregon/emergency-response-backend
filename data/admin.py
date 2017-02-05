from django.contrib import admin
from data.models import Incident, Agency, AlarmLevel, CensusTract, FireBlock

# Register your models here.
admin.site.register(Incident)
admin.site.register(Agency)
admin.site.register(AlarmLevel)
admin.site.register(CensusTract)
admin.site.register(FireBlock)
