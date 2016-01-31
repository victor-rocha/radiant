from django import template

from radiant.pages.models import RadiantPage


register = template.Library()


@register.assignment_tag
def get_page(url):
    try:
        page = RadiantPage.objects.get(url=url)
    except RadiantPage.DoesNotExist:
        page = None
    return page
