from django.db import models


class AbstractRadiantModel(models.Model):
    name = models.CharField(max_length=255, help_text='e.g. Homepage')
    mp4_url = models.CharField(max_length=255, blank=True)
    webm_url = models.CharField(max_length=255, blank=True)
    ogg_url = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        abstract = True
