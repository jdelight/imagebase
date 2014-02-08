from django.contrib import messages
from django.views.generic import CreateView

from image.models import Image

class UploadView(CreateView):
    template_name = 'upload.html'
    model = Image
    fields = ['image']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Image uploaded successfully')
        return super(UploadView, self).form_valid(form)