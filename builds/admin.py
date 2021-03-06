from django.contrib import admin
from builds.models import Build

class BuildAdmin(admin.ModelAdmin):
    list_display = ('project', 'date', 'success')

admin.site.register(Build, BuildAdmin)
