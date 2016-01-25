from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import RadiantPage


class RadiantPageView(DetailView):
    model = RadiantPage

    def get(self, *args, **kwargs):
        self.url = self.kwargs.get('url')
        if not self.url.endswith('/'):
            return HttpResponsePermanentRedirect('{url}/'.format(url=self.url))
        return super(RadiantPageView, self).get(*args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(RadiantPage, url__icontains=self.url)

    def get_template_names(self):
        template_name = 'index.html'
        if self.object:
            template_name = 'pages/{0}'.format(self.object.template_name)
        return [template_name]
