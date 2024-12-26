from django.shortcuts import render
from .models import registration_form
from .forms import user_registration_Form

 
def main(request):
	return render(request, 'main.html')
 

def registration(request):
	context = {
		'registration_form': user_registration_Form,
			}
	
	if request.method == 'POST':
		if request.POST.get('email') and request.POST.get('password'):
				post = registration_form()
				post.user_email = request.POST.get('email')
				post.user_password = request.POST.get('password')
				post.save()
	
	
	return render(request, 'registration.html', context)

def authorization(request):

	context = {
		'authorization_form': user_registration_Form,
			}

	return render(request, 'authorization.html', context)
