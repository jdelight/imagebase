from django.test.testcases import TestCase, Client
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from django.shortcuts import resolve_url

from core.utils import setup_view

from image.views import ImageView
from image.models import Image

class ImageViewTest(TestCase):

    def test_image_url(self):
        view = resolve('/image/1/')
        self.assertEqual(view.func.func_name, ImageView.__name__)

    def test_image_view_uses_correct_template(self):
        view = setup_view(ImageView(), RequestFactory().get('/fake'))
        self.assertEqual(view.get_template_names(), ['image.html'])

    def test_image_view_returns_200(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        client = Client()
        response = client.get(image.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_image_view_template_extends_base(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        client = Client()
        response = client.get(resolve_url(image))
        self.assertTemplateUsed(response, 'base.html')

    def test_image_view_contain_image(self):
        image = Image.objects.create(title='my image', image='my_image.jpg')
        client = Client()
        response = client.get(resolve_url(image))
        self.assertEqual(response.context['image'], image)
