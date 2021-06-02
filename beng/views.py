from django.shortcuts import redirect,render
from .models import Login, Patient, Donor, RequestDonor, RequestOrganizer

def mainpage(request):

	return render(request,'mainpage.html')

def Patient(request):

	usser=Login.objects.create(
		username = request.POST['aaaa'],
		password = request.POST['password'],
		)
	return render(request,'2nd.html')
	return redirect('goods') 

def Donor(request):

	usser=Login.objects.create(
		firstName = request.POST['First'],
		lastName = request.POST['Last'],
		email = request.POST['Email'],
		contactNumber = request.POST['Contact'],
		age = request.POST['Age'],
		gendr = request.POST[('gender','MALE'),('gender','FEMALE')]
		)
	return render(request,'3rd.html')
	return redirect('goods')


# def Item(request):


	
# 	return render(request,'second.html')