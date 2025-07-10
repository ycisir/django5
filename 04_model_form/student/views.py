from django.shortcuts import render
from student.forms import RegistrationForm
from django.http import HttpResponseRedirect

def register(request):
	
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		# print(request.POST)
		if form.is_valid():
			# tmp = form.save(commit=False)
			form.save()
			return HttpResponseRedirect('/student/register/')
	else:
		form = RegistrationForm()

	return render(request, 'student/registration.html', {'form':form})


def success(request):
	return render(request, 'student/success.html')
