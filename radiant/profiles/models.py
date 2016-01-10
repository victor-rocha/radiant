from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from radiant.common.models import AbstractRadiantModel
from .utils import insert_quote


class RadiantHuman(AbstractRadiantModel):
    DRAFT = 0
    LIVE = 1
    UNRELEASED = 2

    STATUS = [
        (DRAFT, 'Draft'),
        (UNRELEASED, 'Unreleased'),
        (LIVE, 'Live'),
    ]
    youtube_url = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(upload_to='radiant-human/', blank=True)
    slider_description = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles_radianthuman_detail', kwargs={'pk': self.id})

    @property
    def is_live(self):
        return self.status == self.LIVE

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
