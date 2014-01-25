from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from core.views import DashboardView
from upload.views import UploadView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagebase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),

    url(r'^admin/', include(admin.site.urls)),
)
