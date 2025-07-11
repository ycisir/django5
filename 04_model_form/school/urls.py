from django.urls import path
from school import views

urlpatterns = [
    path('register/student/', views.student_registeration, name='student_registeration'),
    path('register/teacher/', views.teacher_registeration, name='teacher_registeration'),
]