"""VirtualClassroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vclass.views import *
from account.views import *


urlpatterns = [
    path('',Home, name='home'),
    path('adminorg/', admin.site.urls),
    #path('account/',include('account.urls')),
    path('admin/', Admin,name="admin"),
    path('student/<str:pk>', StudentPage,name="student"),
    path('faculty/<str:pk>', FacultyPage,name="faculty"),
    path('student_profile/<str:pk>', StudentProfile,name="student_profile"),
    path('faculty_profile/<str:pk>', FacultyProfile,name="faculty_profile"),
    path('admin_login/',AdminLogin,name="admin_login"),
    path('faculty_login/',FacultyLogin,name="faculty_login"),
    path('student_login/',StudentLogin,name="student_login"),
    path('admin_logout/',AdminLogout,name="admin_logout"),
    path('faculty_logout/',FacultyLogout,name="faculty_logout"),
    path('student_logout/',StudentLogout,name="student_logout"),
    path('add_dept/',AddDepartment,name="add_dept"),
    path('add_course/',AddCourse,name="add_course"),
    path('add_faculty/',AddFaculty,name="add_faculty"),
    path('add_student/',AddStudent,name="add_student"),
    path('view_course/',ViewCourse,name="view_course"),
    path('view_faculty/',ViewFaculty,name="view_faculty"),
    path('view_student/',ViewStudent,name="view_student"),
    path('view_dept/',ViewDept,name="view_dept"),
    path('course_enroll(?P<str:cid>,?P<str:fid>)',CourseEnroll,name="course_enroll"),

    path('course_faculty/<str:pk>/<str:fid>',CourseFacultyPage,name="course_fac_page"),
    path('course_student/<str:pk>/<str:sid>',CourseStudentPage,name="course_stud_page"),
    path('enroll_students/<str:id>/<str:fid>',EnrollStudents,name="enroll_students"),
    path('show_participants/<str:cid>',ShowParticipants,name="show_participants"),
    path('post_attendance/<str:cid>/<str:fid>',PostAttendance,name="post_attendance"),
    path('give_attendance(?P<str:aid>,?P<str:sid>,?P<str:cid>)',GiveAttendance,name="give_attendance"),
    path('view_attendance_faculty/<str:cid>/<str:fid>/<str:aid>',ViewAttendanceFaculty,name="view_attendance_faculty"),
    path('post_assignment/<str:cid>/<str:fid>',PostAssignment,name="post_assignment"),

    path('view_assignment_faculty/<str:cid>/<str:fid>/<str:aid>',ViewAssignmentFaculty,name="view_assignment_faculty"),
    path('view_assignment_student/<str:cid>/<str:sid>/<str:aid>',ViewAssignmentStudent,name="view_assignment_student"),
    path('grade_assignment(?P<str:sid>,?P<str:cid>,?P<str:fid>,?P<str:aid>)',GradeAssignment,name="grade_assignment"),
    path('post_quiz/<str:cid>/<str:fid>',PostQuiz,name="post_quiz"),
    path('view_quiz_faculty/<str:qid>/<str:cid>/<str:fid>',ViewQuizFaculty,name="view_quiz_faculty"),
    path('view_quiz_student/<str:qid>/<str:cid>/<str:sid>',ViewQuizStudent,name="view_quiz_student"),
    path('add_questions(<str:qid>,<str:cid>,<str:fid>',AddQuestions,name="add_questions"),
    path('delete_quiz(<str:qid>,<str:cid>,<str:fid>)',deletequiz,name="delete_quiz"),
    path('delete_question(<str:qid>,<str:cid>,<str:fid>)',deletequestion,name="delete_question"),
    path('update_quiz(<str:qid>,<str:cid>,<str:fid>)',updatequiz,name="update_quiz"),
    path('quiz_page/<str:qid>/<str:cid>/<str:sid>',QuizPage,name="quiz_page"),
    path('quiz_page/<str:qid>/<str:cid>/<str:sid>/data',QuizDatapage,name="quiz_data_page"),
    path('quiz_page/<str:qid>/<str:cid>/<str:sid>/save',quiz_save_data,name="quiz_save_data"),
]


