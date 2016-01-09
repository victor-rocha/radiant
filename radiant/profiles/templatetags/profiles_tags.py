from django import template

register = template.Library()

from radiant.profiles.models import RadiantHuman


@register.assignment_tag
def get_latest_episodes():
    humans = RadiantHuman.objects.all()
    return humans
