from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import StudentFeedBack, AssingmentHandIn
# Create your views here.

class FeedBackView(CreateView):
    model = StudentFeedBack
    fields = '__all__'
    template_name = 'studentsfeedback.html'

class StudentsDash(TemplateView):
    template_name = 'studentsdash.html'
    

class HandinView(CreateView):
    model = AssingmentHandIn
    fields = '__all__'
    template_name = 'handin.html'