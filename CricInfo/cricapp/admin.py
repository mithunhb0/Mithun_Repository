from django.contrib import admin
from cricapp.models import Cricketer

class CricketerAdmin(admin.ModelAdmin):
    list_display = ('id','name','jersey_number','age','ipl_team')

admin.site.register(Cricketer, CricketerAdmin)
