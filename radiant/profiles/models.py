from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from .utils import insert_quote


class RadiantHuman(models.Model):
    name = models.CharField(max_length=255)
    mp4_url = models.CharField(max_length=255, blank=True)
    webm_url = models.CharField(max_length=255, blank=True)
    ogg_url = models.CharField(max_length=255, blank=True)
    youtube_url = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    slider_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles_radianthuman_detail', kwargs={'pk': self.id})

    def process_content(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        paragraphs = soup.findAll('p')
        break1 = 3
        section_one = paragraphs[:break1]
        quote = self.quote_set.first()
        if quote:
            section_two = insert_quote(paragraphs[break1:], quote.text)
        else:
            section_two = paragraphs[break1:]
        return [
            ' '.join([paragraph.prettify() for paragraph in section_one]),
            ' '.join([paragraph.prettify() for paragraph in section_two]),
        ]


class Quote(models.Model):
    text = models.CharField(max_length=255)
    radiant_human = models.ForeignKey(RadiantHuman, null=True, blank=True)

    def __str__(self):
        return self.text
