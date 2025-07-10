from django.shortcuts import render
from student.forms import Register
from django.http import HttpResponseRedirect

def register(request):
	
	if request.method == 'POST':
		form = Register(request.POST)

		if form.is_valid():
			print(form.cleaned_data)
			# return HttpResponseRedirect('/student/success/')
			return HttpResponseRedirect('/student/register/')
	else:
		form = Register()

	return render(request, 'student/registration.html', {'form':form})


def success(request):
	return render(request, 'student/success.html')
