from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView

class Home(ListView):
    template_name = 'pages/home.html'
    model = Article

class detail(DetailView):
    template_name = 'pages/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


