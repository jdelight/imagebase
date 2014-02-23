import json
from django.views.generic import ListView
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse

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

class DashboardDataView(DashboardView):

    def get(self, *args, **kwargs):

        data = {
            'images': {}
        }

        for image in self.get_queryset():
            data['images'][image.id] = {
                'viewUrl': image.get_absolute_url(),
                'contentUrl': reverse('image_content', args=(image.id,)),
                'updateUrl': reverse('image_update_content', args=(image.id,))
            }

        return HttpResponse(json.dumps(data))