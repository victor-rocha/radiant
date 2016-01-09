from django.conf.urls import patterns, url


from radiant.pages import views


urlpatterns = patterns('',
    url('^(?P<url>.*)$',
        views.RadiantPageView.as_view(),
        name='profiles_radianthuman_detail'),
)
