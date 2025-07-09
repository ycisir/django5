from django import forms

class Registration(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	city = forms.CharField()


class Login(forms.Form):
	email = forms.EmailField(help_text="write your email")
	password = forms.CharField()