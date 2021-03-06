from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from radiant.common.models import AbstractRadiantModel
from radiant.profiles.utils import insert_quote


class RadiantPage(AbstractRadiantModel):
    page_image = models.ImageField(upload_to='radiant-pages/', blank=True)
    youtube_url = models.CharField(max_length=255, blank=True, null=True,
                                   help_text='Page name')
    url = models.CharField(verbose_name='URL', max_length=255,
                           help_text='e.g. contact/ (notice that this value shouldn\'t start with an /',
                           blank=True)
    template_name = models.CharField(max_length=255, default='index.html',
                                     help_text='Available templates: index.html, about.html, contact.html, radiant-humans.html')
    is_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url:
            return reverse('pages_radiantpage_detail', kwargs={'url': self.url})
        return '/'

    def split_content(self):
        """Splits content into two separate objects, one for preview and the other for
        the rest"""
        soup = BeautifulSoup(self.content, 'html.parser')
        paragraphs = soup.findAll('p')
        break1 = 4
        preview = paragraphs[:break1]
        hidden_text = paragraphs[break1:]
        return [
            ' '.join([paragraph.prettify() for paragraph in preview]),
            ' '.join([paragraph.prettify() for paragraph in hidden_text]),
        ]

    def process_content(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        paragraphs = soup.findAll('p')
        quote = self.quote_set.first()
        if quote:
            processed_paragraphs = insert_quote(paragraphs, quote.text)
        else:
            processed_paragraphs = paragraphs
        return ' '.join([paragraph.prettify() for paragraph in processed_paragraphs])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        homepages = RadiantPage.objects.filter(is_homepage=True)
        if not self.url:
            if homepages.count():
                # there can only be one homepage
                homepages.update(is_homepage=False)
        elif not homepages.count():
            # we need to have at least one homepage
            self.url = ''
            self.name = 'Homepage'
        super(RadiantPage, self).save(force_insert=force_insert, force_update=force_update,
                                      using=using, update_fields=update_fields)


class Quote(models.Model):
    text = models.CharField(max_length=255)
    radiant_human = models.ForeignKey(RadiantPage, null=True, blank=True)

    def __str__(self):
        return self.text
