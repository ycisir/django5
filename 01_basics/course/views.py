from django.shortcuts import render

def learn_python(request):
	name = 'python'
	description = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.'
	context = {
		'name': name,
		'description':description,
	}
	return render(request, 'course/python.html', context)


def learn_django(request):
	name = 'django'
	description = 'Django is a free and open-source, Python-based web framework that facilitates rapid development of secure and scalable web applications. It adheres to the model-template-views (MTV) architectural pattern, which is a variation of the more common model-view-controller (MVC) pattern.'
	context = {
		'name': name,
		'description':description,
	}
	return render(request, 'course/django.html', context)