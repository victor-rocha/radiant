from django.views.generic import DetailView, ListView

from radiant.profiles.models import RadiantHuman


class RadiantHumanView(DetailView):
    template_name = 'profiles/radiant_human.html'
    model = RadiantHuman


class RadiantHumanListView(ListView):
    model = RadiantHuman
    template_name = 'profiles/radiant_humans.html'

    def get_queryset(self):
        qs = super(RadiantHumanListView, self).get_queryset()
        return qs.exclude(status=RadiantHuman.DRAFT).order_by('release_date')

    # def
