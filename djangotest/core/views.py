from django.shortcuts import render, redirect
from django.http import HttpResponse as Response
import hashlib
from forms import LoginForm, RegistrationForm
from models import User
# Create your views here.


def index(request):
	# return Response("<center><h1>Hello World!</h1></center>")
	return render(
			request,
			"index.html",
			{"name": "Bingo"}			
		)

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			un = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			h = hashlib.new("md5")
			h.update(pw)
			user = User.objects.filter(username=un,password=h.hexdigest())
			if user:
				return render(request,"authorised.html",{"username":un})
			else:
				return Response("Invalid user")
			
		else:
			return Response("Invalid form")
	else:
		 form = LoginForm()
		 return render(
		 	request, 
		 	"login.html",
		 	{"form":form}
		)

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			un = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			h = hashlib.new("md5")
			h.update(pw)
			user = User(username=un,password=h.hexdigest())
			user.save()
			return redirect("/login")			
		else:
			return Response("Invalid form")
	else:
		 form = RegistrationForm()
		 return render(
		 	request, 
		 	"register.html",
		 	{"form":form}
		)
