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

    def get_context_data(self, **kwargs):
        ctx = super(RadiantHumanListView, self).get_context_data(**kwargs)
        episodes = ctx['object_list']
        current_episodes_index = episodes.filter(status=RadiantHuman.LIVE).count()
        ctx['current_episodes_index'] = current_episodes_index
        return ctx
