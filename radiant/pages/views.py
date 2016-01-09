from django.views.generic import DetailView

from .models import RadiantPage


class RadiantPageView(DetailView):
    model = RadiantPage

    def get_object(self, queryset=None):
        url = self.kwargs.get('url')
        if url:
            page = RadiantPage.objects.get(url=url)
        else:
            page = RadiantPage.objects.get(url='')
        return page

    def get_template_names(self):
        return ['pages/index.html']
