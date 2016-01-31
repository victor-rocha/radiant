from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from radiant.common.models import AbstractRadiantModel, AbstractBaseModel
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
    slider_image = models.ImageField(upload_to='radiant-human/', blank=True)
    homepage_thumbnail = models.ImageField(upload_to='radiant-human/', blank=True,
                                           help_text='Image should be 638x666 px (width x height)')
    dropdown_thumbnail = models.ImageField(upload_to='radiant-human/', blank=True)
    filmstrip_image = models.ImageField(upload_to='radiant-human/', blank=True)
    homepage_blurb = models.ImageField(upload_to='radiant-human/', blank=True)
    blurb_image = models.TextField(blank=True, null=True)
    slider_description = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    ordering = models.IntegerField(default=1)

    class Meta:
        ordering = ('ordering', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.status == self.LIVE:
            return reverse('profiles_radianthuman_detail', kwargs={'pk': self.id})
        return ''

    def has_homepage_image(self):
        return True if self.homepage_thumbnail else False
    has_homepage_image.boolean = True

    def has_dropdown_image(self):
        return True if self.dropdown_thumbnail else False
    has_dropdown_image.boolean = True

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


class TeamMemberManager(models.Manager):
    use_for_related_fields = True

    def producers(self):
        return self.filter(role=self.model.PRODUCER).order_by('id')

    def editors(self):
        return self.filter(role=self.model.EDITOR).order_by('id')

    def developers(self):
        return self.filter(role=self.model.DEVELOPER).order_by('id')

    def designers(self):
        return self.filter(role=self.model.DESIGNER).order_by('id')


class TeamMember(AbstractBaseModel):
    PRODUCER = 1
    EDITOR = 2
    DEVELOPER = 3
    DESIGNER = 4
    ROLES = (
        (PRODUCER, 'Director'),
        (EDITOR, 'Editor'),
        (DEVELOPER, 'Developer'),
        (DESIGNER, 'Designer'),
    )

    name = models.CharField(max_length=255)
    role = models.IntegerField(choices=ROLES)
    thumbnail = models.ImageField(upload_to='team/', blank=True)
    blurb = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)
    page = models.ForeignKey('pages.RadiantPage', null=True, blank=True)
    ordering = models.IntegerField(default=1)
    objects = TeamMemberManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('ordering', )
