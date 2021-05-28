from django.shortcuts import render
from .models import reg_table
from .models import login_table
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# Create your views here.
def index_fun(request):
	return render(request,'index.html')

def register(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		pas=request.POST["password"]
		mob=request.POST["mob"]
		state=request.POST["state"]
		dist=request.POST["dist"]
		city=request.POST["city"]
		a=reg_table(Name=name,Email=email,Password=pas,Mobile=mob,State=state,Dist=dist,City=city,Status="pending")
		a.save()
		return render(request,'login.html')
	else:
		return render(request,'register.html')

def login(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		chk=reg_table.objects.filter(Email=username,Password=password)
		if chk:
			for x in chk:
				request.session['id']=x.id
				return render(request,'Edu_home.html')
		else:
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def admin_login(request):
	if request.method=="POST":
		uname=request.POST["uname"]
		pas=request.POST["pas"]
		b=login_table.objects.filter(Username=uname,Password=pas)
		if b:
			for x in b:
				request.session['id']=x.id
				return render(request,'ad_home.html')
		else:
			return render(request,'index.html')
	else:
		return render(request,'admin_login.html')

def view(request):
	d=reg_table.objects.all()
	return render(request,'pending.html',{'views':d})

def approve(request):
	e=request.GET['id']
	r=reg_table.objects.all().filter(id=e).update(Status="Approved")
	return HttpResponseRedirect('/pending/')

def reject(request):
	e=request.GET['id']
	r=reg_table.objects.all().filter(id=e).update(Status="Rejected")
	return HttpResponseRedirect('/pending/')

def delete(request):
	e=request.GET['id']
	r=reg_table.objects.all().filter(id=e).delete()
	return HttpResponseRedirect('/pending/')

def Edu_logout(request):
	del request.session['id']
	logout(request)
	return HttpResponseRedirect('/')

def view_profile(request):
	s=request.session['id']
	f=reg_table.objects.all().filter(id=s)
	return render(request,'view_profile.html',{'data':f})

def update(request):
	if request.method=="POST":
		s=request.session['id']
		name=request.POST["name"]
		email=request.POST["email"]
		password=request.POST["pass"]
		phone=request.POST["ph"]
		state=request.POST["state"]
		dist=request.POST["dist"]
		city=request.POST["city"]
		a=reg_table.objects.all().filter(id=s).update(Name=name,Email=email,Password=password,Mobile=phone,State=state,Dist=dist,City=city)
		return HttpResponseRedirect('/view_profile/')
	else:
		s=request.session['id']
		f=reg_table.objects.all().filter(id=s)
		return render(request,'update.html',{'data':f})

def upload(request):
	return render(request,'stud_dataset.html')


def predict(request):
	return render(request,'prediction.html')