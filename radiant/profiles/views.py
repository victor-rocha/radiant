import json

from django.core import serializers
from django.views.generic import DetailView, ListView

from radiant.profiles.models import RadiantHuman


class RadiantHumanView(DetailView):
    template_name = 'profiles/radiant_human.html'
    model = RadiantHuman


class RadiantHumanListView(ListView):
    model = RadiantHuman
    template_name = 'profiles/radiant_humans.html'

    def get_context_data(self, **kwargs):
        ctx = super(RadiantHumanListView, self).get_context_data(**kwargs)
        episodes = serializers.serialize('json', self.model.objects.all())
        ctx['episodes'] = episodes
        return ctx
