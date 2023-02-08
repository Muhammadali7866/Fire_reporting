from django.contrib import admin
from .models import add_team,fire_report,fire_history
# Register your models here.
admin.site.register(add_team)
admin.site.register(fire_report)
admin.site.register(fire_history)