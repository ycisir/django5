from django.urls import path
from scanner import views

urlpatterns = [
	path('generate/', views.generate, name='generate'),
	path('scan/', views.scan, name='scan'),
]