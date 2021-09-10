from django.urls import path
from hero.views import HulkView, IronManView, BlackWidowView, HomeView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
    path('', HomeView.as_view())
]