from django.shortcuts import render
from django.views.generic import FormView, TemplateView

class UploadView(TemplateView):
    template_name = 'upload.html'
    # form_class = None

