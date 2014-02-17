from django.contrib import messages
from django.views.generic import UpdateView

from .models import ImagebaseSettings

class SettingsView(UpdateView):
    template_name = 'settings.html'
    model = ImagebaseSettings

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Settings updated successfully')
        return super(SettingsView, self).form_valid(form)

    def get_object(self, queryset=None):
        return ImagebaseSettings.objects.get_or_create()[0]
