from django.urls import path
from student import views

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
]