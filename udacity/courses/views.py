from django.shortcuts import render, redirect
from .models import DummyDetails

posts=[
	{
		"userId":1,
		"id":1,
		"title":"django",
		"body":"django Content"

	},
	{
		"userId":2,
		"id":2,
		"title":"Python",
		"body":"python Content"

	},
	{
		"userId":3,
		"id":3,
		"title":"HTML",
		"body":"HTML Content"

	},
	{
		"userId":1,
		"id":14,
		"title":"Flask",
		"body":"Flask Content"

	},
]
users=[
	{
		
		"id":1,
		"name":"Prasanna Raj",
		"body":"django Content"

	},
	{
		
		"id":2,
		"name":"Mallipudi",
		"body":"python Content"

	},
]

# Create your views here.
def home(request):
	contex={
		'posts':posts,
		'users':users

	}
	return render(request,"courses/home.html",contex)

def details(request):
	details=DummyDetails.objects.all()
	contex = {
		'details':details
	}
	return render(request,"courses/viewDetails.html",contex)

def addDetails(request):
	if request.method == 'POST':
		details = DummyDetails(name = request.POST['name'],
			mobile = request.POST['mobile'],
			email = request.POST['email'],
			gender = request.POST['gender'])
		details.save()
		return redirect('/courses/details')
	else:
		return render(request,'courses/addDetails.html')

def editDetails(request, dummy_id):
	if request.method == 'POST':
		getDummy = DummyDetails.objects.get(id = dummy_id)
		getDummy.name = request.POST['name']
		getDummy.mobile = request.POST['mobile']
		getDummy.email = request.POST['email']
		getDummy.gender = request.POST['gender']
		getDummy.save()
		return redirect('/courses/details')
	else:
		getDummy = DummyDetails.objects.get(id = dummy_id)
		context = {"details" : getDummy}
		return render(request, 'courses/editDetails.html', context)
def deleteDetails(request,dummy_id):
	getDummy = DummyDetails.objects.get(id = dummy_id)
	getDummy.delete()
	return redirect('/courses/details')