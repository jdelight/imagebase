from django.test import TestCase
from django.core.urlresolvers import reverse

from image.models import Image

class ImageModelTest(TestCase):
    def test_image_model(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        self.assertEqual(image.title, 'my image')
        self.assertEqual(image.image, 'my_image.jpg')
        self.assertEqual(str(image), 'my image')

    def test_image_get_absolute_url(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        image_url = image.get_absolute_url()
        self.assertEqual(image_url, '/image/1/')


    def test_image_url_resolves_to_get_absolute_url(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        image_url = reverse('image', args=[image.id])
        self.assertEqual(image_url, image.get_absolute_url())
