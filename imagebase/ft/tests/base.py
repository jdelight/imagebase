import os
from StringIO import StringIO
from PIL import Image as PIL_Image
from django.core.files.uploadedfile import UploadedFile

from django.test import LiveServerTestCase
from django.conf import settings
from selenium import webdriver

class ImagebaseLiveServerTestCase(LiveServerTestCase):
    """
    Base class for functional tests
    """

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        super(ImagebaseLiveServerTestCase, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        super(ImagebaseLiveServerTestCase, self).tearDownClass()


    def get_uploaded_file(self):
        """
        Returns an uploaded file instance for testing
        """
        file = StringIO()
        uploaded_image = PIL_Image.new('RGBA',size=(400,400), color=(255,0,0))
        uploaded_image.save(file, 'jpeg')
        file.name = 'test.jpg'
        return UploadedFile(file=file)


    def _save_screenshot(self, screenshot_filename):
        filename = os.path.join(settings.BASE_DIR, 'imagebase/ft/tests/screenshots/%s' % screenshot_filename)
        self.browser.get_screenshot_as_file(filename)
