from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import user

# Create your views here.
def index(request):
	return render(request,'portfo/index.html')
def about(request):
	return render(request,'portfo/about.html')

def contact(request):
	return render(request,'portfo/contact.html')

def get_value(request):
	if request.method=='POST':
		email=request.POST.get('email')
		sub=request.POST.get('subject')
		text=request.POST.get('textarea')
		use=user()
		use.email=email
		use.subject=sub
		use.text=text
		use.save()
	return render(request,'portfo/thankyou.html')