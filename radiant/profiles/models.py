from bs4 import BeautifulSoup

from django.db import models


class RadiantHuman(models.Model):
    name = models.CharField(max_length=255)
    mp4_url = models.CharField(max_length=255, blank=True)
    webm_url = models.CharField(max_length=255, blank=True)
    ogg_url = models.CharField(max_length=255, blank=True)
    youtube_url = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def process_content(self):
        soup = BeautifulSoup(self.content)
        paragraphs = soup.findAll('p')
        return [
            ' '.join([paragraph.prettify() for paragraph in paragraphs[:4]]),
            ' '.join([paragraph.prettify() for paragraph in paragraphs[4:-1]]),
        ]


class Quote(models.Model):
    text = models.CharField(max_length=255)
    radiant_human = models.ForeignKey(RadiantHuman, null=True, blank=True)

    def __str__(self):
        return self.text
