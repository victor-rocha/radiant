from django import template

from radiant.profiles.models import RadiantHuman


register = template.Library()


@register.assignment_tag
def get_latest_episodes():
    live_episodes = RadiantHuman.objects.filter(status=RadiantHuman.LIVE).order_by('-release_date')[:2]
    unreleased_episode = RadiantHuman.objects.filter(status=RadiantHuman.UNRELEASED).order_by('release_date').first()
    episodes = [episode for episode in live_episodes]
    episodes.append(unreleased_episode)
    return episodes


@register.assignment_tag
def get_episodes():
    return RadiantHuman.objects.all()


@register.assignment_tag
def past_released_episodes():
    return RadiantHuman.objects.filter(status=RadiantHuman.LIVE)


@register.assignment_tag
def upcoming_released_episodes():
    return RadiantHuman.objects.filter(status=RadiantHuman.LIVE)


@register.assignment_tag
def released_episodes_count():
    return RadiantHuman.objects.filter(status=RadiantHuman.LIVE).count()
