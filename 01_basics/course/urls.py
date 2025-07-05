from django.urls import path
from course import views

urlpatterns = [
    path('learn_django/', views.learn_django, name='learn_django'),
]