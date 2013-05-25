from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^get_data$', views.get_data),
    url(r'^file_user$', views.file_user),
    url(r'^feedback$', views.feedback),
    # Examples:
    # url(r'^$', 'UA.views.home', name='home'),
    # url(r'^UA/', include('UA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
