from django.urls import path
from course import views

urlpatterns = [
    path('django/', views.django, name='django'),
    path('python/', views.python, name='python'),
]