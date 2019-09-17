from django import forms
from .models import Signup

class SignupForm(forms.Form):
	your_name = forms.CharField(label = 'Your_name', max_length = 100)
	email = forms.EmailField(label = 'Email', max_length = 100)
	gender = forms.CharField(label = 'Gender', max_length = 10)
	no = forms.IntegerField(label = 'No')
	Qua = forms.CharField(label = 'Qua', max_length = 50)
	branch = forms.CharField(label = 'Branch', max_length = 100)
	code = forms.CharField(label = 'Code', max_length = 25)
	ccode = forms.CharField(label = 'ccode', max_length = 25)
	

	'''class Meta:
		model =  Signup
		fields = ('FullName','Email','Gender','PhoneNumber','Qualification','Branch','password','conPassword')'''