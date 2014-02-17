from django.views.generic import ListView

from image.models import Image
from prefs.models import ImagebaseSettings

class DashboardView(ListView):

    template_name = 'dashboard.html'
    model = Image

    def get_imagebase_settings(self):
        # get_or_create returns a tuple so we only want the first item (the object)
        imagebase_setting = ImagebaseSettings.objects.get_or_create()
        return imagebase_setting[0]

    def get_queryset(self):
        return self.model.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['imagebase_settings'] = self.get_imagebase_settings()
        return context