from django.shortcuts import render
from .models import Post
 
def main(request):
	return render(request, 'main.html')
 
def registrarion(request):
	return render(request, 'registration.html')

def authorization(request):
	return render(request, 'authorization.html')
