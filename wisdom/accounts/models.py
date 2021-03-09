from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length= 255 , null= True , blank= True)
    last_name = models.CharField(max_length=255 , null= True , blank= True)
    email = models.EmailField(unique= True)
    reg_number = models.CharField(max_length=255 , null= True , blank= True)
    student =  models.BooleanField(default= False)
    staff = models.BooleanField(default= False)
    admin = models.BooleanField(default= False)
    active = models.BooleanField(default= False)

USERNAME_FEILD = 'email'
REQUIRED_FEILDS = []

def __str__(self):
    return self.email

def get_full_name(self):
    return self('first_name' + 'last_name')

@property
def is_staff(self):
    return self.staff

@property
def is_admin(self):
    return self.admin

@property
def is_student(self):
    return self.student