from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

class Home(ListView):
    template_name = 'pages/home.html'
    model = Article
