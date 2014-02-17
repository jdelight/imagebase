from django.db import models
from django.core.urlresolvers import reverse

class ImagebaseSettings(models.Model):
    show_id = models.BooleanField(default=False)
    show_title = models.BooleanField(default=True)
    show_tags = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('setting', args=[self.id])