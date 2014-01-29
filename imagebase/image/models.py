from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imagebase')
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('image', args=[self.id])