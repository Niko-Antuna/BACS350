from django.urls import path
from django.contrib import admin
from hero.views import IndexView, HeroDeleteView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView
from django.urls.conf import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',                        IndexView.as_view(), name='index_view'),
    path('hero/',                   HeroListView.as_view(), name='hero_list'),
    path('hero/<int:pk>',           HeroDetailView.as_view(), name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/',          HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(), name='hero_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),
]
