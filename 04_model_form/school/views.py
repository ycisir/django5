from django.shortcuts import render
from school.forms import StudentRegistration, TeacherRegistration

def student_registeration(request):
	if request.method == 'POST':
		form = StudentRegistration(request.POST)
		print(request.POST)
	else:
		form = StudentRegistration()

	context = {
		'form': form,
	}

	return render(request, 'school/student.html', context)



def teacher_registeration(request):
	if request.method == 'POST':
		form = TeacherRegistration(request.POST)
		print(request.POST)
	else:
		form = TeacherRegistration()

	context = {
		'form': form,
	}

	return render(request, 'school/teacher.html', context)
