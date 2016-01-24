from django.contrib import admin

from radiant.contacts.models import Contact, Subscriber


class ContactAdmin(admin.ModelAdmin):
    search_fields = ['email', 'full_name', 'message']
    list_display = ['full_name', 'email']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber)
