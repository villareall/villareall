from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
def Russex(request):
	
	if request.method == 'POST':
		
		name = request.POST['name']
		subject = request.POST['subject']
		body = request.POST['body']
		gender = request.POST['gender']
		date = request.POST['date']

		
		rus = Item()
		rus.name = name
		rus.subject = subject
		rus.body = body
		rus.gender = gender
		rus.date = date
		rus.save()


	return render(request,'weh.html')


def Page(request):
	rus = Item.objects.all().order_by('date')
	return render(request,'dada.html', {'rus': rus})