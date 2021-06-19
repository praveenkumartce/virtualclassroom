from django.db import models
from django_mysql.models import ListCharField
from django.conf import settings
from datetime import *
from django.utils import timezone
User = settings.AUTH_USER_MODEL
import random
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=35)
    faculty_nos=models.IntegerField(default=0)
    course_nos=models.IntegerField(default=0)
    student_nos = models.IntegerField( default=0)
    since=models.DateField()
    def __int__(self):
        return self.dep_id

class AttendanceSubmission(models.Model):
    id=models.CharField(primary_key=True,max_length=25)
    student=models.ForeignKey('account.Student',on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    stamp=models.DateTimeField(null=True)
    def __str__(self):
        return self.id
import uuid
class Attendance(models.Model):
    att_id=models.AutoField(primary_key=True)
    #att_students=models.ManyToManyField('account.Student')
    sub=models.ManyToManyField(AttendanceSubmission)
    att_hour=models.CharField(max_length=20)
    att_date=models.DateField(default=timezone.now())
    att_start=models.DateTimeField(default=timezone.now())
    att_end=models.DateTimeField(default=timezone.now())
    att_duration=models.IntegerField(default=10)
    att_code=models.CharField(
        unique=True,
        editable=False,max_length=6)
    print(att_code)

    def __int__(self):
        return self.att_id

    def active(self):

        now = timezone.now()
        print(now)
        print(self.att_start)
        print(self.att_end)
        if self.att_start <= now and now <= self.att_end:
            print("true")
            return True
        print("false")
        return False
sub=FileSystemStorage(location='vclass/static/assignment_submissions')
class SubmissionFiles(models.Model):
    id=models.AutoField(primary_key=True)
    sub_files=models.FileField(storage=sub)

    def __int__(self):
        return self.id
class Submission(models.Model):
    id=models.CharField(primary_key=True,max_length=25)
    files=models.ManyToManyField(SubmissionFiles)
    date=models.DateTimeField(null=True)
    graded=models.BooleanField(default=False)
    marks=models.IntegerField(null=True)
    student=models.ForeignKey('account.Student',on_delete=models.CASCADE)
    def __str__(self):
        return self.id

fs_ass=FileSystemStorage(location='vclass/static/assignment')
class Assignment(models.Model):
    ass_id=models.AutoField(primary_key=True)
    ass_name=models.CharField(max_length=20)
    ass_desc=models.CharField(max_length=100,default="")
    ass_file=models.FileField(max_length=255,null=True,storage=fs_ass)
    submissions=models.ManyToManyField(Submission)
    ass_posted=models.DateTimeField()
    ass_due=models.DateTimeField()
    #ass_students=models.ManyToManyField('account.Student')
    def __int__(self):
        return self.ass_id
    def active(self):
        now = timezone.now()

        if self.ass_posted <= now and now <= self.ass_due:
            print("true")
            return True
        print("false")
        return False

class Courses(models.Model):
    course_id=models.CharField(primary_key=True,max_length=30)
    course_name=models.CharField(max_length=50)
    dep_id=models.ForeignKey(Department,on_delete=models.CASCADE,default=1)
    course_atts = models.ManyToManyField(Attendance)
    course_assign=models.ManyToManyField(Assignment)
    course_faculty =models.CharField(max_length=200,default="")
    course_students = models.ManyToManyField('account.Student')
    part_count=models.IntegerField(default=0)
    def __str__(self):
        return self.course_id
    def get_quizzes(self):
        return self.quiz_set.all()


class Quiz(models.Model):
    quiz_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=40)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    duration=models.IntegerField(help_text="duration in minutes")
    no_of_questions=models.IntegerField(default=0)

    def __int__(self):
        return self.quiz_id
    def get_results(self):
        return self.quizresult_set.all()
    def active(self):
        now = timezone.now()
        # print(now)
        # print(self.start_time)
        # print(self.end_time)
        if self.start_time <= now and now <= self.end_time:
            return True
        return False
    def get_all_questions(self):
        return self.quizquestion_set.all()
    def get_questions(self):
        questions=list(self.quizquestion_set.all())
        random.shuffle(questions)
        return questions[:self.no_of_questions]

correct_choice=(
    ('option1','option1'),('option2','option2'),('option3','option3'),('option4','option4'),)

class QuizQuestion(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    option1=models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct = models.CharField(max_length=300)
    def __int__(self):
        return self.question_id

class QuizResult(models.Model):
    id=models.AutoField(primary_key=True)
    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    student_id = models.ForeignKey('account.Student',on_delete=models.CASCADE)
    score=models.IntegerField(null=True)
    stamp=models.DateTimeField(null=True)
    status=models.BooleanField(default=False)

    def __int__(self):
        return self.id