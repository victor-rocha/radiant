from django.contrib import admin

from radiant.profiles.models import RadiantHuman, Quote


class QuoteInline(admin.StackedInline):
    model = Quote
    max_num = 1


class RadiantHumanAdmin(admin.ModelAdmin):
    inlines = [QuoteInline]


admin.site.register(RadiantHuman, RadiantHumanAdmin)
