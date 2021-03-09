from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from center.models import Course,TeachersDetail,Units,StudentsDetail
from accounts.models import User

# Create your models here.
class Grades(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='+')
    date = models.DateTimeField(auto_now_add = True)
    results = models.IntegerField(null= True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='+')
    assign = models.FileField(null=True)
    date = models.DateTimeField(auto_now_add = True)
    handindate = models.DateField(auto_now_add = True)
    comment = models.TextField()

    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class StudentAttendence(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='+')
    name = models.ForeignKey(User, on_delete= models.CASCADE, related_name='+')
    studntsnames = models.ForeignKey(StudentsDetail , on_delete= models.CASCADE, related_name='+')


    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])

        