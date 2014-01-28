from django.shortcuts import render
from django.views.generic import ListView

from image.models import Image

class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = Image
