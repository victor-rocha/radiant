from django.db import models
from django.core.urlresolvers import reverse

from radiant.common.models import AbstractRadiantModel


class RadiantPage(AbstractRadiantModel):
    url = models.CharField(verbose_name='URL', max_length=255,
                           help_text='Once set, this shouldn\'t be changed.',
                           blank=True)
    template_name = models.CharField(max_length=255, default='index.html',
                                     help_text='Available templates: index.html, about.html, contact.html')
    is_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pages_radiantpage_detail', kwargs={'url': self.url})

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
