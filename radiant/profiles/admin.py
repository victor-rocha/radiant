from django.contrib import admin

from radiant.profiles.models import RadiantHuman, Quote


class QuoteInline(admin.StackedInline):
    model = Quote
    max_num = 1


class RadiantHumanAdmin(admin.ModelAdmin):
    inlines = [QuoteInline]
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('status',)
    list_display = ('name', 'ordering', 'release_date', 'status', 'has_homepage_image',
                    'has_dropdown_image',)
    fieldsets = (
        (None, {
            'fields': ('writer', 'name', 'title', 'content',
                       'slider_description', 'release_date', 'status', 'ordering')
        }),
        ('Media (Images/Video)', {
            'fields': ('mp4_video', 'webm_video', 'ogg_video', 'youtube_url',
                       'slider_image', 'homepage_thumbnail', 'dropdown_thumbnail',
                       'filmstrip_image', 'blurb_image'),
        }),
        ('Social Media', {
            'fields': ('og_title', 'og_type', 'og_description', 'og_image'),
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )


admin.site.register(RadiantHuman, RadiantHumanAdmin)
