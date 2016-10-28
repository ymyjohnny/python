from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'logparsertest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logs/', include('logs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
