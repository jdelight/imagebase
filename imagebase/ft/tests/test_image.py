from django.conf import settings

from base import ImagebaseLiveServerTestCase

from image.models import Image

class ImageTest(ImagebaseLiveServerTestCase):
    pass
    # def test_image_view_shows_image(self):
    #     image = Image.objects.create(title='title', image='image.jpg')
    #     image_url = image.get_absolute_url()
    #     full_image_url = self.live_server_url + image_url
    #     self.browser.get(full_image_url)
    #
    #     main_image = self.browser.find_elements_by_class_name('main_image')[0]
    #     self.assertEqual(main_image.get_attribute('src'), self.live_server_url + settings.MEDIA_URL + 'image.jpg')
