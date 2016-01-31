import datetime
import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User


def get_upload_path(instance, filename):
    return os.path.join('videos/', str(uuid4()), filename)


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super(AbstractBaseModel, self).save(**kwargs)

    class Meta:
        abstract = True


class AbstractRadiantModel(AbstractBaseModel):
    writer = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField('Tab\'s title', max_length=255, help_text='e.g. Homepage')
    title = models.CharField(max_length=255, help_text='This is the title for articles, etc.',
                             blank=True)
    mp4_video = models.FileField(upload_to=get_upload_path, max_length=255, blank=True)
    webm_video = models.FileField(upload_to=get_upload_path, max_length=255, blank=True)
    ogg_video = models.FileField(upload_to=get_upload_path, max_length=255, blank=True)
    content = models.TextField(blank=True)
    mata_description = models.CharField(max_length=144, blank=True)

    # facebook metatags
    og_title = models.CharField('og:title', max_length=255, blank=True, null=True,
                                help_text='Facebook share title')
    og_type = models.CharField('og:title', max_length=255, blank=True, null=True,
                               default='article')
    og_description = models.CharField('og:description', max_length=255, blank=True,
                                      null=True, help_text='Facebook share description')
    og_image = models.ImageField(upload_to='ogtags/', blank=True,
                                 help_text='An image has to be at least 50px by 50px, '
                                           'but preferably bigger than 200px by 200px. '
                                           'Plus, the image can’t be more than 5 MB in size.')

    class Meta:
        abstract = True
