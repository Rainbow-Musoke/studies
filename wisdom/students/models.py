from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from center.models import StudentsDetail,Course,Units
from accounts.models import User

# Create your models here.
class StudentFeedBack(models.Model):
    title = models.CharField(max_length= 200)
    name = models.ForeignKey(User, on_delete= models.CASCADE, related_name='+')
    feedback = models.TextField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feedback', args=[str(self.id)])



class AssingmentHandIn(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='+')
    course_unit = models.ForeignKey(Units, on_delete= models.CASCADE, related_name='+')
    handin = models.FileField(null = True)
    date = models.DateTimeField(auto_now_add = True) 


    def __str__(self):
        return self.course_unit

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])

        