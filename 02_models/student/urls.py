from django.urls import path
from student import views

urlpatterns = [
    path('all/', views.all_data, name='all_data'),
    path('<int:id>/', views.single_data, name='single_data'),
]