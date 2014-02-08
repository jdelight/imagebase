from django.views.generic import ListView

from image.models import Image

class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = Image

    def get_queryset(self):
        return self.model.objects.all().order_by('-created')
