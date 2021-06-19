from django.db import models
from django.contrib.auth.models import AbstractUser
from django_mysql.models import ListCharField
from vclass.models import *

#from django.utils.crypto import get_random_string
import uuid

# Create your models here.
class User(AbstractUser):
    is_faculty=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    faculty_id=models.CharField(primary_key=True,max_length=8,unique=True)
    faculty_name = models.CharField(max_length=35)
    fac_dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty_deg=models.CharField(max_length=50)
    courses_enrolled=models.IntegerField(default=0)
    enrolled = models.ManyToManyField(Courses)

    since=models.DateField()
    def __str__(self):
        return self.faculty_id

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(primary_key=True,max_length=8,unique=True)
    student_name = models.CharField(max_length=35)
    stud_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrolled =models.ManyToManyField(Courses)
    join_date=models.DateField()
    def __str__(self):
        return self.student_id

