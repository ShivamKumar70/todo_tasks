from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request , "newyear/index.html")

def greet(request,name):
	return render(request , "newyear/greet.html" ,
		{
		"name" : name
		})

