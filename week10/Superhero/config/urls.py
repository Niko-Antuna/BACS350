from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from hero.views_hero import HeroView

path('accounts/', include('django.contrib.auth.urls')),
path('accounts/', include('accounts.urls')),
path('', RedirectView.as_view(url='accounts/'), name='home'),

path('admin/', admin.site.urls),

path('', include('hero.urls')),

path('', include('doc.urls')),
