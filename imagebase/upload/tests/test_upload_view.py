from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve

from core.utils import setup_view
from image.models import Image

from upload.views import UploadView

class UploadViewTest(TestCase):

    def test_upload_url_resolves_to_upload_view(self):
        view = resolve('/upload/')
        self.assertEqual(view.func.func_name, UploadView.__name__)

    def test_upload_view_uses_correct_template(self):
        upload_request = RequestFactory().get('/foo')
        upload_view = UploadView()
        view = setup_view(upload_view, upload_request)
        template_names = view.get_template_names()
        self.assertEqual(template_names, ['upload.html'])

    def test_upload_view_renders_successfully(self):
        client = Client()
        response = client.get('/upload/')
        self.assertEqual(response.status_code, 200)

    def test_upload_view_template_extends_base(self):
        client = Client()
        response = client.get('/upload/')
        self.assertTemplateUsed(response, 'base.html')

    def test_upload_view_contains_title(self):
        client = Client()
        response = client.get('/upload/')
        self.assertContains(response, 'Imagebase: Upload')

    def test_upload_view_success_url_returns_image_model_url(self):
        image = Image.objects.create(title='title', image='image.jpg')
        upload_request = RequestFactory().get('/foo')
        upload_view = UploadView()
        upload_view.object = image
        view = setup_view(upload_view, upload_request)
        self.assertEqual(view.get_success_url(), image.get_absolute_url())


