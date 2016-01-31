from urllib.parse import urlparse
from urllib.parse import parse_qs

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
def get_current_episode():
    live_episode = RadiantHuman.objects.filter(status=RadiantHuman.LIVE).order_by('-release_date').first()
    if live_episode:
        return RadiantHuman.objects.filter(status=RadiantHuman.LIVE).order_by('-release_date').first()
    return RadiantHuman.objects.filter(status=RadiantHuman.UNRELEASED).order_by('release_date').first()


@register.assignment_tag
def get_next_episode():
    live_episode = RadiantHuman.objects.filter(status=RadiantHuman.LIVE).order_by('-release_date').first()
    if live_episode:
        return RadiantHuman.objects.filter(status=RadiantHuman.UNRELEASED).order_by('release_date').first()
    return RadiantHuman.objects.filter(status=RadiantHuman.UNRELEASED).order_by('release_date')[1]


@register.assignment_tag
def released_episodes_count():
    return RadiantHuman.objects.filter(status=RadiantHuman.LIVE).count() or 1


@register.filter
def youtube_embed(url):
    """Converts a regular youtube url into a embeddable one"""
    parsed_url = urlparse(url)
    qs = parse_qs(parsed_url.query)
    return "https://www.youtube.com/embed/{video_id}?rel=0&wmode=transparent&showinfo=1&autohide=1".format(video_id=qs.get('v', [''])[0])
