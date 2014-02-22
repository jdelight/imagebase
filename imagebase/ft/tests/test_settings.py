from base import ImagebaseLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException

from prefs.models import ImagebaseSettings
from image.models import Image

class SettingsTests(ImagebaseLiveServerTestCase):

    def test_user_can_update_image_attribute_settings(self):

        # create our settings
        ImagebaseSettings.objects.create(show_title=True, show_id=True, show_tags=True)

        image = Image.objects.create(id=1, title='image title', image=self.get_uploaded_file())
        image.tags.add('tag1', 'tag2')


        response = self.browser.get(self.live_server_url)
        attributes_container_id = 'image_%s_attributes' % image.id

        image_attributes = self.browser.find_element_by_id(attributes_container_id)

        image_attributes_title = image_attributes.find_element_by_class_name('attr_title').text
        image_attributes_id = image_attributes.find_element_by_class_name('attr_id').text
        image_attributes_tags = image_attributes.find_element_by_class_name('attr_tags').text

        self.assertEqual('TITLE\nimage title', image_attributes_title)
        self.assertEqual('ID\n1', image_attributes_id)
        self.assertIn('tag1', image_attributes_tags)
        self.assertIn('tag2', image_attributes_tags)

        self.browser.get(self.live_server_url + '/settings/1/')

        settings_form = self.browser.find_element_by_id('settings_form')
        show_title = self.browser.find_element_by_id('id_show_title')

        # should be initially checked
        self.assertTrue(show_title.is_selected())
        show_title.click()

        # confirm clicking unselects the checkbox
        self.assertFalse(show_title.is_selected())

        # submit the form
        settings_form.submit()

        # checkbox should be unselected after submission
        show_title = self.browser.find_element_by_id('id_show_title')
        self.assertFalse(show_title.is_selected())

        # helpful message should be shown
        self.assertIn('Settings updated successfully', self.browser.page_source)


        self.browser.get(self.live_server_url)

        image_attributes = self.browser.find_element_by_id(attributes_container_id)

        with self.assertRaises(NoSuchElementException):
            image_attributes.find_element_by_class_name('attr_title')

        image_attributes_id = image_attributes.find_element_by_class_name('attr_id').text
        image_attributes_tags = image_attributes.find_element_by_class_name('attr_tags').text

        self.assertEqual('ID\n1', image_attributes_id)
        self.assertIn('tag1', image_attributes_tags)
        self.assertIn('tag2', image_attributes_tags)







