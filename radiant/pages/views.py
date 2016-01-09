from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import RadiantPage


class RadiantPageView(DetailView):
    model = RadiantPage

    def get_object(self, queryset=None):
        return get_object_or_404(RadiantPage, url=self.kwargs.get('url'))

    def get_template_names(self):
        return ['pages/index.html']
