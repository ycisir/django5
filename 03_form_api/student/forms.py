from django import forms
from django.core.validators import MinLengthValidator

class Registration(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	city = forms.CharField()


class Login(forms.Form):
	email = forms.EmailField(help_text="write your email")
	password = forms.CharField()



GENDER_CHOICES = [
	('M','Male'), 
	('F', 'Female'), 
	('O', 'Other')
]

INTEREST_CHOICES = [
	('tech', 'Technology'), 
	('art', 'Arts'), 
	('sports', 'Sports')
]

class DemoForm(forms.Form):
	name = forms.CharField(
		label='Full name',
		max_length=50,
		label_suffix=':',
		# initial='Enter full name',
		help_text='Enter you legal name',
		validators=[MinLengthValidator(5)],
		widget=forms.TextInput(attrs={'placeholder':'Your name', 'class':'my_css'})
	)
	email = forms.EmailField()
	pin_code = forms.IntegerField()

	age = forms.FloatField()
	date_of_birth = forms.DateField()
	appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
	appointment_datetime = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local', 'placeholder':'YYYY-MM-DD HH:MM:SS'}))
	is_subscribed = forms.BooleanField()
	agree = forms.NullBooleanField()

	gender = forms.ChoiceField(choices=GENDER_CHOICES)
	interests = forms.MultipleChoiceField(choices=INTEREST_CHOICES)

	profile_image = forms.ImageField()
	resume = forms.FileField()
	portfolio = forms.URLField()

	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
	password = forms.CharField(widget=forms.PasswordInput())
	slug = forms.SlugField()
	ip_address = forms.GenericIPAddressField()
	rating = forms.DecimalField()
