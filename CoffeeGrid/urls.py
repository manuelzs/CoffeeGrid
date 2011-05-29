from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CoffeeGrid.views.home', name='home'),
    # url(r'^CoffeeGrid/', include('CoffeeGrid.foo.urls')),

    # Home
    url(r'^$', 'dashboard.views.dashboard'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Accounts
    url(r'^accounts/', include('registration.urls')),

    # Facebook
    (r'^facebook/', include('facebookconnect.urls')),

    # User Profiles
    url(r'^(?P<username>[a-z]+)$','userprofiles.views.profile'),
)

urlpatterns += patterns('', (r'^badges/', include('badges.urls')), )
