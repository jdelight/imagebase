from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve
from prefs.views import SettingsView

from core.utils import setup_view

from prefs.models import ImagebaseSettings

class PrefsTests(TestCase):

    def test_settings_url_resolves_to_settings_view(self):
        settings_view = resolve('/settings/1/')
        self.assertEqual(SettingsView.__name__, settings_view.func.func_name)

    def test_settings_view_uses_settings_template(self):
        settings_request = RequestFactory().get('/settings/1/')
        settings_view = SettingsView()
        view = setup_view(settings_view, settings_request)
        template_names = view.get_template_names()
        self.assertEqual(template_names, ['settings.html'])

    def test_settings_view_renders_successfully(self):
        client = Client()
        response = client.get('/settings/1/')
        self.assertEqual(response.status_code, 200)

    def test_settings_extends_base(self):
        client = Client()
        response = client.get('/settings/1/')
        self.assertTemplateUsed(response, 'base.html')

    def test_settings_view_contains_settings_form(self):
        client = Client()
        response = client.get('/settings/1/')
        self.assertIn('form', response.context)


    def test_setting_view_contains_setting_form(self):
        imagebase_settings = ImagebaseSettings.objects.create(show_title=False, show_id=True, show_tags=True)
        url = imagebase_settings.get_absolute_url()
        response = self.client.get(url)
        form_instance = response.context['form'].instance
        self.assertTrue(isinstance(form_instance, ImagebaseSettings))



