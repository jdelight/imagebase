import os
import tempfile
import shutil

from django.conf import settings
from django.test.utils import override_settings

from base import ImagebaseLiveServerTestCase

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class UploadTest(ImagebaseLiveServerTestCase):

    small_image_file = os.path.join(settings.BASE_DIR, 'imagebase/ft/tests/test_data/1x1.gif')
    medium_image_file = os.path.join(settings.BASE_DIR, 'imagebase/ft/tests/test_data/scene.jpg')

    @classmethod
    def setUpClass(self):
        if not os.path.isdir(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)
        super(UploadTest, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(MEDIA_ROOT)
        super(UploadTest, self).tearDownClass()


    def test_user_can_upload_image(self):
        self.browser.get(self.live_server_url+'/upload/')
        self.assertEqual('Imagebase: Upload', self.browser.title)

        upload_form = self.browser.find_element_by_class_name('upload_form')
        upload_form.find_element_by_id('id_image').send_keys(self.small_image_file)
        upload_form.submit()

        self.assertRegexpMatches(self.browser.current_url, self.live_server_url + '/image/[0-9]+/')
        self.assertIn('Image uploaded successfully', self.browser.page_source)


    def test_uploaded_image_is_resized(self):
        self.browser.get(self.live_server_url+'/upload/')
        self.assertEqual('Imagebase: Upload', self.browser.title)

        upload_form = self.browser.find_element_by_class_name('upload_form')
        upload_form.find_element_by_id('id_image').send_keys(self.medium_image_file)
        upload_form.submit()

        self.assertRegexpMatches(self.browser.current_url, self.live_server_url + '/image/[0-9]+/')
        image = self.browser.find_element_by_class_name('main_image_large')
        self.assertEqual(image.size['width'], 300)


    def test_user_can_edit_image(self):
        self.browser.get(self.live_server_url+'/upload/')
        self.assertEqual('Imagebase: Upload', self.browser.title)

        upload_form = self.browser.find_element_by_class_name('upload_form')
        upload_form.find_element_by_id('id_image').send_keys(self.medium_image_file)
        upload_form.submit()

        self.assertRegexpMatches(self.browser.current_url, self.live_server_url + '/image/[0-9]+/')

        self.browser.find_element_by_link_text('edit image').click()

        update_form = self.browser.find_element_by_class_name('update_form')
        update_form.find_element_by_id('id_title').send_keys('image title')
        update_form.submit()

        self.assertRegexpMatches(self.browser.current_url, self.live_server_url + '/image/[0-9]+/$')

        title_text = self.browser.find_element_by_class_name('heading').text
        self.assertEqual(title_text, 'image title')

    def test_user_can_delete_image(self):
        self.browser.get(self.live_server_url+'/upload/')
        self.assertEqual('Imagebase: Upload', self.browser.title)

        upload_form = self.browser.find_element_by_class_name('upload_form')
        upload_form.find_element_by_id('id_image').send_keys(self.medium_image_file)
        upload_form.submit()

        self.assertRegexpMatches(self.browser.current_url, self.live_server_url + '/image/[0-9]+/')

        self.browser.find_element_by_link_text('delete image').click()



