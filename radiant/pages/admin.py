from django.contrib import admin

from radiant.pages.models import RadiantPage


class RadiantPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(RadiantPage, RadiantPageAdmin)
