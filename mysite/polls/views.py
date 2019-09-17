from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm
# Create your views here.
'''def index(request):
	return HttpResponse("hello world")
def home(request):
	return render(request, 'signup.html')'''


def get(request):
	if request.method == 'POST':

		form = SignupForm(request.POST)

		if form.is_valid():
			your_name = form.cleaned_data['FullName']
			email = form.cleaned_data['Email']
			gender = form.cleaned_data['Gender']
			no = form.cleaned_data['PhoneNumber']
			Qua = form.cleaned_data['Qualification']
			branch = form.cleaned_data['branch']
			code = form.cleaned_data['password']
			ccode = form.cleaned_data['conPassword']
			#form.save()
			return HttpResponseRedirect('/signup.html/')

		
	return render(request, 'signup.html',context = {'form': form})