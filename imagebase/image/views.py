from django.contrib import messages
from django.views.generic import UpdateView, ListView, DetailView

from taggit.models import Tag

from .models import Image

class ImageView(DetailView):
    template_name = 'image.html'
    model = Image

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        related_images = Image.objects.filter(tags__name__in=list(self.object.tags.all())).distinct().exclude(id__exact=self.object.id)
        context['related_images'] = related_images
        return context

class ImageUpdateView(UpdateView):
    template_name = 'image_update.html'
    model = Image
    fields = ['image', 'title', 'tags']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Image updated successfully')
        return super(ImageUpdateView, self).form_valid(form)


class ImageTagView(ListView):
    template_name = 'tags.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(ImageTagView, self).get_context_data(**kwargs)
        tag = self.kwargs.get('slug')
        images = Image.objects.filter(tags__name__in=[tag])
        context['images'] = images
        context['tag_slug'] = tag
        return context