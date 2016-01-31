from django.conf.urls import patterns, url

from radiant.contacts.views import ContactView, SubscribeView, NominateView


urlpatterns = patterns('',
    url('^contact-us/', ContactView.as_view(),
        name='contact-us'),
    url('^subscribe/', SubscribeView.as_view(),
        name='subscribe'),
    url('^nominate/', NominateView.as_view(),
        name='nominate'),
)
