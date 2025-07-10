from django.shortcuts import render
from student.forms import Register
from django.http import HttpResponseRedirect
from student.models import Profile

def register(request):
	
	if request.method == 'POST':
		form = Register(request.POST)

		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')

			user = Profile(name=name, email=email, password=password)
			# user = Profile(id=1, name=name, email=email, password=password) #update
			user.save()
			# user.delete(id=2)

			# return HttpResponseRedirect('/student/success/')
			return HttpResponseRedirect('/student/register/')
	else:
		form = Register()

	return render(request, 'student/registration.html', {'form':form})


def success(request):
	return render(request, 'student/success.html')
