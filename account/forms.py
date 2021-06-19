from django.contrib.auth.forms import UserCreationForm
from vclass.models import  *
from django.db import  transaction
from .models import *
from django import forms
class FacultyReg(UserCreationForm):
    print("1 in console")
    faculty_id = forms.CharField(required=True)
    faculty_name = forms.CharField(required=True)
    fac_dept = forms.CharField(required=True)
    faculty_deg = forms.CharField(required=True)
    since = forms.DateField();
    print(1)
    class Meta(UserCreationForm.Meta):
        model=User
    @transaction.atomic
    def data_save(self):
        user=super().save(commit=False)
        user.is_faculty=True
        user.save();
        faculty=Faculty.objects.create(user=user)
        faculty.faculty_id=self.cleaned_data.get('faculty_id')
        faculty.faculty_name=self.cleaned_data.get('faculty_name')
        faculty.fac_dept=self.cleaned_data.get('fac_dept')
        faculty.faculty_deg=self.cleaned_data.get('faculty_deg')
        faculty.since==self.cleaned_data.get('since')
        faculty.save()
        return faculty
class StudentReg(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student=True
        user.save();
        student = Faculty.objects.create(user=user)
        student.student_id = self.cleaned_data.get('student_id')
        student.student_name= self.cleaned_data.get('student_name')
        student.stud_dept = self.cleaned_data.get('stud_dept')
        student.join_date == self.cleaned_data.get('join_date')
        student.save()
        return student