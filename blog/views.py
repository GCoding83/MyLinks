from django.shortcuts import render

# Create your views here.
# PERSO: A "view" is a subset of a database which is stored as a permanent object

def home(request):
	#The third (optional) argument is "context", which allows you to use variables from Python inside your html file.
	return render(request, 'blog/blog-home.html')
