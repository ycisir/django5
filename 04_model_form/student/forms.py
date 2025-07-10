from django import forms
from student.models import Profile

class RegistrationForm(forms.ModelForm):
	confirm_password = forms.CharField()
	class Meta:
		model = Profile
		fields = ('name', 'email', 'password')
		# fields = '__all__'
		# exlude = ('name',)
		labels = {
			'name': 'Full name'
		}
		error_messages = {
			'name': {
				'required': 'Name required'
			},
			'email': {
				'required': 'Email required'
			},
			'password': {
				'required': 'Password required'
			}
		}
		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'my_class',
				'placeholder': 'Your full name'
			}),
			'email': forms.EmailInput(attrs={
				'class': 'my_class',
				'placeholder': 'Your email'
			}),
			'password': forms.PasswordInput(attrs={
				'class': 'my_class',
				'placeholder': 'Your password'
			})
		}
