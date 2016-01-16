from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from radiant.common.models import AbstractRadiantModel
from radiant.profiles.utils import insert_quote


class RadiantPage(AbstractRadiantModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(verbose_name='URL', max_length=255,
                           help_text='Once set, this shouldn\'t be changed.',
                           blank=True)
    template_name = models.CharField(max_length=255, default='index.html',
                                     help_text='Available templates: index.html, about.html, contact.html')
    is_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url:
            return reverse('pages_radiantpage_detail', kwargs={'url': self.url})
        return '/'

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
