from django.contrib import admin
from account.models import User,Student,Faculty
from .models import *
# Register your models here.
#admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Courses)

admin.site.register(Attendance)
admin.site.register(Assignment)
admin.site.register(AttendanceSubmission)
admin.site.register(Submission)
admin.site.register(SubmissionFiles)

admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizResult)