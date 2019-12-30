from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
	username=request.session.get('username','')
	if user != '':
		return render(request,"home.html",{'usernm':username})
	else:
		return render(request,'home.html')

def event(request):
	return render(request,'event.html')

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request,"login.html",c)

def signup(request):
	cs = {}
	cs.update(csrf(request))
	return render(request,"signup.html",cs)

def auth_view(request):
	username = request.POST.get('username')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		#request.session['username']=username
		auth.login(request,user)
		return render(request,'home.html',{'usernm':username})
	else:
		return HttpResponseRedirect('/mytrip/login/')

def create(request):
	User = get_user_model()
	row = 0
	uname = request.POST.get('username', '')
	emailid = request.POST.get('email', '')
	fname = request.POST.get('firstname', '')
	lname = request.POST.get('lastname', '')
	mobile = request.POST.get('phone', '')
	pword = request.POST.get('password', '')
	pword1 = request.POST.get('password1', '')
	for p in User.objects.raw('SELECT * FROM mytrip_users where username = %s',[uname]):
		row = row + 1
		
	if row != 0:
		return render(request,'login.html',context={'exist':"tyu"})
		
	if pword == pword1:
		user = User.objects.create_user(uname, emailid, pword, first_name=fname, last_name=lname, mobileno=mobile)
	else:
		return render(request,'signup.html',context={'user':uname})
	request.session['username']=uname
	if user is not None:
			user.save();
			auth.login(request,user)
			return render(request,'home.html',{'usernm':uname})
	else:
		print("enter correct details")
		return HttpResponseRedirect('/mytrip/signup/')

def logout(request):
	#del request.session['username']
	auth.logout(request)
	return render(request,'home.html')

