from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve

from core.utils import setup_view
from core.views import DashboardView

from image.models import Image

class DashboardViewTest(TestCase):

    def test_root_url_resolves_to_dashboard_view(self):
        view = resolve('/')
        self.assertEqual(view.func.func_name, DashboardView.__name__)

    def test_root_url_returns_dashboard_template(self):
        dashboard_request = RequestFactory().get('/')
        dashboard_view = DashboardView()
        view = setup_view(dashboard_view, dashboard_request)
        dashboard_view.object_list = []
        template_names = view.get_template_names()
        self.assertEqual(template_names, ['dashboard.html'])

    def test_dashboard_view_renders_successfully(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_template_extends_base(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_dashboard_view_with_no_images(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Upload an image')

    def test_dashboard_view_contains_imagebase_settings_in_context(self):
        client = Client()
        response = client.get('/')
        self.assertIn('imagebase_settings', response.context)

    def test_dashboard_view_imagebase_settings_returns_single_row(self):
        client = Client()
        response = client.get('/')
        imagebase_settings = response.context['imagebase_settings']
        self.assertTrue(hasattr(imagebase_settings, 'show_title'))
        self.assertTrue(hasattr(imagebase_settings, 'show_id'))
        self.assertTrue(hasattr(imagebase_settings, 'show_tags'))

    def test_dashboard_view_with_attributes_off(self):

        imagebase_settings = {
            'show_title': False,
            'show_id': False,
            'show_tags': False
        }
        image = Image.objects.create(id=12345, title='1234image_title')
        image.tags.add('1234_tag1')
        image.save()

        request = RequestFactory().get('/')
        DashboardView.get_imagebase_settings = lambda get_imagebase_settings: imagebase_settings
        dashboard_view = DashboardView.as_view()
        dashboard_view.object_list = [image]
        response = dashboard_view(request)

        self.assertNotContains(response, 'title: 1234image_title')
        self.assertNotContains(response, 'tags: 1234_tag1')
        self.assertNotContains(response, 'id: 12345')

