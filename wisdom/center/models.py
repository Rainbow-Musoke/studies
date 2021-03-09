from django.db import models
from django.urls import reverse
from django.conf import settings
from accounts.models import User


# Create your models here.
class Course(models.Model):
    program = models.CharField(max_length= 30, null= False)

    def __str__(self):
        return self.program

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class Units(models.Model):
    course = models.ForeignKey(Course,on_delete= models.CASCADE, related_name='+')
    year = models.IntegerField(null = False)
    sem = models.IntegerField(null= False)
    course_units = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class Tuition(models.Model):
    course = models.ForeignKey(Course, null = False, on_delete = models.CASCADE, related_name='+')
    tution = models.IntegerField(null = False)

    def __str___(self):
        return self.course

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class StudentsDetail(models.Model):
    student_pic = models.ImageField(null = True)
    name = models.CharField(max_length=30, null=False, blank= False)
    date_birth = models.DateField()
    reg_number = models.CharField(max_length= 50, null = False, blank= False)
    fees = models.ForeignKey(Tuition, null= False, on_delete= models.CASCADE)
    course = models.ForeignKey(Course,on_delete= models.CASCADE, related_name='+')
    year = models.IntegerField(null= False)
    sem = models.IntegerField(null= False)

    def __str__(self):
        return self.reg_nummber

    def get_absolute_url(self):
        return reverse('students', args=[str(self.id)])


class TeachersDetail(models.Model):
    teacher_pic = models.ImageField(null = True )
    name = models.CharField(max_length=30, null=False, blank= False)
    reg_nummber = models.CharField(max_length= 50, null = False, blank= False)
    teacher_course = models.ForeignKey(Course,on_delete= models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])



class TeacherAttendence(models.Model):
    name = models.ForeignKey(User, on_delete= models.CASCADE)
    course = models.ForeignKey(Course,null = True, on_delete= models.CASCADE, related_name='+')
    teachersname = models.ForeignKey(TeachersDetail,null=True, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])




