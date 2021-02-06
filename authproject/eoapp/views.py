from django.shortcuts import render,redirect

# Create your views here.

def home(request):
	request.session.modified = True
	if 'name' in request.session:
		return render(request,'home.html')
	else:
		return render(request,'ulogin.html')