from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def setting_home(request):
	
	return render(request,'setting_home.html',{})   