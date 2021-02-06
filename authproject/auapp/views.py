from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def usignin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw1=request.POST.get('pw1')
		pw2=request.POST.get('pw2')

		if pw1==pw2:
			try:
				usr=User.objects.get(username=un)
				return render(request,'usignup.html',{'msg':'user already exists with this username'})
			except User.DoesNotExist:
				usr=User.objects.create_user(username=un,password=pw1)
				usr.save()
				return redirect('ulogin')
		else:
			return render(request,'usignup.html',{'msg':'Passwords Dosent match'})

	else:
		return render(request,'usignup.html')		

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw=request.POST.get('pw')
		usr=authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'Invalid login'})
		else:
			login(request,usr)
			request.session['name']=un
			return redirect('home')

	else:
			return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	request.session.flush()
	request.session.clear_expired()
	return redirect('ulogin')