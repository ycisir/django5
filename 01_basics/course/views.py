from django.shortcuts import render
from datetime import datetime

def learn_django(request):
	name = 'django'
	description = 'Django is a free and open-source, Python-based web framework that facilitates rapid development of secure and scalable web applications. It adheres to the model-template-views (MTV) architectural pattern, which is a variation of the more common model-view-controller (MVC) pattern.'
	date = datetime.now()
	p1 = '59.24321'
	p2 = '59.000'
	p3 = '59.37000'
	context = {
		'name': name,
		'description':description,
		'date':date,
		'p1':p1,
		'p2':p2,
		'p3':p3,
	}
	return render(request, 'course/django.html', context)