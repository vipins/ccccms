from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin, comments
import captcha
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^comments/', include('captcha.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
