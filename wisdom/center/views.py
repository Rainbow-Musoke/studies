from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(CreateView):
    template_name = 'contact.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FeedBackView(ListView):
    template_name = 'feedback.html'