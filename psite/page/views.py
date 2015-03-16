from django.shortcuts import render

# Create your views here.
def index(requset):
	return render(requset, 'page/index.html')

def lin(requset):
	return render(requset, 'page/lin.html')

def about(request):
	return render(request, 'page/about.html')