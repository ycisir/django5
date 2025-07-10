from django import forms
from django.core import validators

# custom validators
def gmail_only(value):
	if not value.split('@')[1] == 'gmail.com':
		raise forms.ValidationError('gmail domain needed!')

class Register(forms.Form):
	name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(4)])
	email = forms.EmailField(validators=[gmail_only])
	password = forms.CharField(widget=forms.PasswordInput())


	# single validation
	# def clean_email(self):
	# 	# email_value = self.cleaned_data['email']
	# 	email_value = self.cleaned_data.get('email')

	# 	gmail_domain = email_value.split('@')[1]
		
	# 	if not gmail_domain == 'gmail.com':
	# 		raise forms.ValidationError('gmail domain needed!!!')

	# 	return email_value


	# validate all at once
	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	name_value = self.cleaned_data.get('name')
	# 	email_value = self.cleaned_data.get('email')

	# 	if name_value and len(name_value) < 5:
	# 		self.add_error('name', 'Should be more than 5 characters!')

	# 	if email_value and email_value.split('@')[1] != 'gmail.com':
	# 		self.add_error('email', 'Gmail domain needed!')

	# 	return cleaned_data