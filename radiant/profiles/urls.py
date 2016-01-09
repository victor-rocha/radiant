from django.conf.urls import patterns, url


from radiant.profiles import views


urlpatterns = patterns('',
    url('^(?P<pk>[\d]+)/$',
        views.RadiantHumanView.as_view(),
        name='profiles_radianthuman_detail'),
    url('^$',
        views.RadiantHumanListView.as_view(),
        name='profiles_radianthuman_list'),
)
