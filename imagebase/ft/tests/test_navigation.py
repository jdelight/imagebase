from base import ImagebaseLiveServerTestCase

class NavigationTest(ImagebaseLiveServerTestCase):

    def test_dashboard_link(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Dashboard').click()
        self.assertEqual('Imagebase: Dashboard', self.browser.title)

    def test_upload_link(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Upload').click()
        self.assertEqual('Imagebase: Upload', self.browser.title)

    def test_settings_link(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Settings').click()
        self.assertEqual('Imagebase: Settings', self.browser.title)
