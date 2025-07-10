from django.shortcuts import render
from student.forms import Registration, Login, DemoForm

def registration(request):
	form = Registration()
	context = {
		'form': form,
	}
	return render(request, 'student/registration.html', context)


def login(request):
	# form = Login()
	form = Login(auto_id='login_%s')
	# form = Login(auto_id=True)	# remove id_
	# form = Login(auto_id=False) # without label tag
	# field_order, label_suffix, initial={'name':'somevalue'}
	context = {
		'form': form,
	}
	return render(request, 'student/login.html', context)


def demo_form(request):
	form = DemoForm()
	return render(request, 'student/demo.html', {'form':form})