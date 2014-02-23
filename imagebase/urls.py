from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


from core.views import DashboardView, DashboardDataView
from upload.views import UploadView
from image.views import ImageView, ImageTagView, ImageUpdateView, ImageDeleteView
from prefs.views import SettingsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagebase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/data/$', DashboardDataView.as_view(), name='dashboard_data'),
    url(r'^dashboard/(.*?)$', DashboardView.as_view(), name='dashboard'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'^image/(?P<pk>\d+)/content/$', ImageView.as_view(template_name='image_content.html'), name='image_content'),
    url(r'^image/(?P<pk>\d+)/panel/$', ImageView.as_view(template_name='image_panel_content.html'), name='image_panel_content'),
    url(r'^image/(?P<pk>\d+)/$', ImageView.as_view(), name='image'),
    url(r'^image/(?P<pk>\d+)/update/$', ImageUpdateView.as_view(), name='image_update'),
    url(r'^image/(?P<pk>\d+)/update/content/$', ImageUpdateView.as_view(template_name='image_update_content.html'), name='image_update_content'),
    url(r'^image/(?P<pk>\d+)/delete/$', ImageDeleteView.as_view(), name='image_delete'),
    url(r'^tags/$', ImageTagView.as_view(), name='image_tag'),
    url(r'^tags/(?P<slug>[\w\-]+)/$', ImageTagView.as_view(), name='image_tag_list'),
    url(r'^settings/(?P<pk>\d+)/$', SettingsView.as_view(), name='setting'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
