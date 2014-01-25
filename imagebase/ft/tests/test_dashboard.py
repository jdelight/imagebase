from base import ImagebaseLiveServerTestCase

class DashboardTest(ImagebaseLiveServerTestCase):

    def test_dashboard_page(self):
        self.browser.get(self.live_server_url)
        self.assertEqual('Imagebase: Dashboard', self.browser.title)
