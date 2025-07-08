from django.shortcuts import render
from student.models import Profile

def all_data(request):
	students = Profile.objects.all()
	context = {
		'students': students
	}
	return render(request, 'student/all.html', context)


def single_data(request, id):
	student = Profile.objects.get(pk=id)
	context = {
		'student': student
	}
	return render(request, 'student/single.html', context)