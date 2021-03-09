from django.shortcuts import render
from .models import StudentAttendence, Assignment, Grades
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class AttendenceView(CreateView):
    model = StudentAttendence
    fields = '__all__'
    template_name = 'attendence.html'

class AssingmentView(CreateView):
    model = Assignment
    fields = '__all__'
    template_name = 'assignments.html'

class GradesView(CreateView):
    model = Grades
    fields = '__all__'
    template_name = 'grades.html'