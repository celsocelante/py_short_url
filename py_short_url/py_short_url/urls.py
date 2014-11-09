from django.conf.urls import *
from django.contrib import admin
from shortener.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'py_short_url.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', index),
    url(r'^api/([^/]+)',api_view),
    url(r'([^/]+)', index_view),
)
