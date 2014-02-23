from django.contrib import messages
from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.core.urlresolvers import reverse_lazy

from taggit.models import Tag


from prefs.models import ImagebaseSettings
from .models import Image
from .forms import ImageDeleteForm

class ImageView(DetailView):
    template_name = 'image.html'
    model = Image

    def get_imagebase_settings(self):
        # get_or_create returns a tuple so we only want the first item (the object)
        # duplicated in the DashboardView - in a real application this wouldn't be done
        imagebase_setting = ImagebaseSettings.objects.get_or_create()
        return imagebase_setting[0]


    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        related_images = Image.objects.filter(tags__name__in=list(self.object.tags.all())).distinct().exclude(id__exact=self.object.id)
        context['related_images'] = related_images
        context['imagebase_settings'] = self.get_imagebase_settings()
        return context

class ImageUpdateView(UpdateView):
    template_name = 'image_update.html'
    model = Image
    fields = ['image', 'title', 'tags']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Image updated successfully')
        return super(ImageUpdateView, self).form_valid(form)


class ImageDeleteView(DeleteView):
    template_name = 'image_delete.html'
    model = Image
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super(ImageDeleteView, self).get_context_data(**kwargs)
        context['form'] = ImageDeleteForm
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Image deleted successfully')
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
