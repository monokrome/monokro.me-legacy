from django.conf.urls.defaults import *
from monokrome.views import Home
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home(), name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
