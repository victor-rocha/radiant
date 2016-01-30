from django.contrib import admin

from radiant.pages.models import RadiantPage, Quote
from radiant.profiles.models import TeamMember


class QuoteInline(admin.StackedInline):
    model = Quote
    max_num = 1


class MemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1
    exclude = ['created_at', 'updated_at']


class RadiantPageAdmin(admin.ModelAdmin):
    inlines = [QuoteInline, MemberInline]
    readonly_fields = ('created_at', 'updated_at',)
    fieldsets = (
        (None, {
            'fields': ('writer', 'name', 'title', 'content',)
        }),
        ('Media (Images/Video)', {
            'fields': ('mp4_video', 'webm_video', 'ogg_video', 'youtube_url', 'page_image'),
        }),
        ('Social Media', {
            'fields': ('og_title', 'og_type', 'og_description', 'og_image'),
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
        ('Victor only', {
            'classes': ('collapse',),
            'fields': ('url', 'template_name', 'is_homepage'),
        }),
    )


admin.site.register(RadiantPage, RadiantPageAdmin)
