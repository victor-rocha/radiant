from django.views.generic import DetailView, ListView

from radiant.profiles.models import RadiantHuman


class RadiantHumanView(DetailView):
    template_name = 'profiles/radiant_human.html'
    model = RadiantHuman


class RadiantHumanListView(ListView):
    model = RadiantHuman
    template_name = 'profiles/radiant_humans.html'
