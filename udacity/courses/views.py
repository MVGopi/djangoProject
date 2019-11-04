from django.shortcuts import render,redirect
from .models import Details
# from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request,'courses/home.html')
def dummydetails(request):
	details=Details.objects.all()
	context={
	'details':details
	}
	return render(request,'courses/dummydetails.html',context)
def Adddummies(request):
	if request.method == "POST":
		details=Details(name=request.POST['name'],age=request.POST['age'],email=request.POST['email'],gender=request.POST['gender'])
		details.save()
		context={'data':"Hello Form"}
		return redirect('/udacity/dummy')
	else:
		return render(request,'courses/addDetails.html')
def names(request):
	details=Details.objects.all()
	context={
	'details':details
	}
	return render(request,'courses/names.html',context)
def editdetails(request,dummy_id):
	if request.method=="POST":
		getDummy=Details.objects.get(id=dummy_id)
		getDummy.name=request.POST['name']
		getDummy.age=request.POST['age']
		getDummy.gender=request.POST['gender']
		getDummy.email=request.POST['email']
		getDummy.save()
		return redirect('/udacity/dummy')
	else:
		getDummy=Details.objects.get(id=dummy_id)
		context={'details':getDummy}
		return render(request,'courses/editdetails.html',context)	
def deletedetails(request,del_id):
	getDelete=Details.objects.get(id=del_id)
	getDelete.delete()
	return redirect('/udacity/dummy')
