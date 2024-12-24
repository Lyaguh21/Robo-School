from django.shortcuts import render
from .forms import user_email_Form, user_password_Form
 
def main(request):
	return render(request, 'main.html')
 
def registration(request):

	context = {
		'email': user_email_Form(),
		'password': user_password_Form()
			}
	
	return render(request, 'registration.html', context)

def authorization(request):

	context = {
		'email': user_email_Form(),
		'password': user_password_Form()
			}

	return render(request, 'authorization.html', context)
