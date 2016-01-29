from django.db import models
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

from radiant.common.models import AbstractBaseModel


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.send_message()
        super(Contact, self).save(force_insert=force_insert, force_update=force_update,
                                  using=using, update_fields=update_fields)

    def send_message(self):
        from_email = self.email
        to = settings.RECIPIENTS
        subject = "You got mail!"
        context = {'message': self.message, 'full_name': self.full_name}
        html_content = render_to_string('contacts/email/message.html', context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject, text_content, from_email, to)
        email.attach_alternative(html_content, "text/html")
        sent = email.send()
        return sent


class Subscriber(AbstractBaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Nominee(AbstractBaseModel):
    radiant_nominee_name = models.CharField(max_length=255)
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='radiant-human/videos/', max_length=255, blank=True)
