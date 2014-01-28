from django.test import LiveServerTestCase
from selenium import webdriver

class ImagebaseLiveServerTestCase(LiveServerTestCase):
    """
    Base class for functional tests
    """

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()
        super(ImagebaseLiveServerTestCase, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        super(ImagebaseLiveServerTestCase, self).tearDownClass()