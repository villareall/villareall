from django.shortcuts import redirect,render
from .models import donor, blooddetails, bloodbank, hospital, employee, bloodrequest

def mainpage(request):

	return render(request,'home.html')
	return redirect('goods') 

def Patient(request):


	return render(request,'donor.html')
# 	return redirect('goods') 

def Donor(request):

	return render(request,'bank.html')
# 	return redirect('goods')


def request(request):

	return render(request,'request.html')

def about(request):

	return render(request,'about.html')