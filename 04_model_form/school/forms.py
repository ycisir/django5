from django import forms
from school.models import Profile


class StudentRegistration(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ('teacher_name',)


class TeacherRegistration(StudentRegistration):
	class Meta(StudentRegistration.Meta):
		exclude = ('student_name',)