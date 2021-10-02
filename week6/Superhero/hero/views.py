from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView
from .models import Hero


class IndexView(TemplateView):
    template_name = 'index.html'


class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Hero
    fields = ['name', 'description', 'image']


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['name', 'description', 'image']


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
