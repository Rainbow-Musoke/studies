from django.contrib import admin
from .models import Assignment, StudentAttendence,Grades

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Grades)
admin.site.register(StudentAttendence)
