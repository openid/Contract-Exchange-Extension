from django.conf.urls.defaults import *
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

SPEC_ROOT = os.path.join( os.path.dirname( os.path.dirname(__file__) ),'spec')
SPEC_FILE = 'openid-cx.draft-3.html'

urlpatterns = patterns('',
    # Example:
    # (r'^doc/', include('doc.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.static.serve', {'document_root': os.path.join( os.path.dirname(__file__),'build/html'),'path':'index.html',}),
    (r'^spec/$', 'django.views.static.serve', {'document_root': SPEC_ROOT ,'path': SPEC_FILE,}),
    (r'(?P<path>.*)', 'django.views.static.serve', {'document_root': os.path.join( os.path.dirname(__file__),'build/html'),}),
)
