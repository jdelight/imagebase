from django.test import TestCase, Client, RequestFactory

from prefs.models import ImagebaseSettings
from prefs.views import SettingsView

class SettingsFormTests(TestCase):



    def test_form_post_returns_redirect(self):
        imagebase_setting = ImagebaseSettings.objects.create(show_title=False, show_id=False, show_tags=False)
        response = self.client.post('/settings/1/', {
            'show_title': True,
            'show_id': True,
            'show_tags': True,
        })

        self.assertEqual(302, response.status_code)


    def test_form_post_with_model_instance(self):

        imagebase_setting = ImagebaseSettings.objects.create( show_title=False, show_id=False, show_tags=False)

        self.assertFalse(imagebase_setting.show_title)
        self.assertFalse(imagebase_setting.show_id)
        self.assertFalse(imagebase_setting.show_tags)

        self.client.post(imagebase_setting.get_absolute_url(), {
            'show_title': '1',
            'show_id': '1',
            'show_tags': '1',
        })

        updated_setting = ImagebaseSettings.objects.get(pk=imagebase_setting.id)

        self.assertTrue(updated_setting.show_title)
        self.assertTrue(updated_setting.show_id)
        self.assertTrue(updated_setting.show_tags)




