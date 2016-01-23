from django.db import models


class AbstractRadiantModel(models.Model):
    name = models.CharField(max_length=255, help_text='e.g. Homepage')
    mp4_video = models.FileField(upload_to='radiant-human/videos/', max_length=255, blank=True)
    webm_video = models.FileField(upload_to='radiant-human/videos/', max_length=255, blank=True)
    ogg_video = models.FileField(upload_to='radiant-human/videos/', max_length=255, blank=True)
    content = models.TextField(blank=True)

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
