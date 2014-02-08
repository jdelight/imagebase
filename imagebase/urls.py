from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


from core.views import DashboardView
from upload.views import UploadView
from image.views import ImageView, ImageTagView, ImageUpdateView, ImageDeleteView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagebase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'^image/(?P<pk>\d+)/$', ImageView.as_view(), name='image'),
    url(r'^image/(?P<pk>\d+)/update/$', ImageUpdateView.as_view(), name='image_update'),
    url(r'^image/(?P<pk>\d+)/delete/$', ImageDeleteView.as_view(), name='image_delete'),
    url(r'^tags/$', ImageTagView.as_view(), name='image_tag'),
    url(r'^tags/(?P<slug>[\w\-]+)/$', ImageTagView.as_view(), name='image_tag_list'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
