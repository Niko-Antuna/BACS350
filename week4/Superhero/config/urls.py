from django import urls
from hero.views import IndexView, HeroListView
from django.contrib import admin
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view()),
]