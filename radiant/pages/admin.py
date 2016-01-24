from django.contrib import admin

from radiant.pages.models import RadiantPage, Quote


class QuoteInline(admin.StackedInline):
    model = Quote
    max_num = 1


class RadiantPageAdmin(admin.ModelAdmin):
    inlines = [QuoteInline]
    raw_id_fields = ('writer', )


admin.site.register(RadiantPage, RadiantPageAdmin)
