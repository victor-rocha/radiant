from django.conf.urls import patterns, url

from radiant.contacts.views import ContactView


urlpatterns = patterns('',
    url('^contact-us/', ContactView.as_view(),
        name='contact-us'),
)
