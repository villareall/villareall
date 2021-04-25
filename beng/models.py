from django.db import models

class Item(models.Model):
	#SECTION
	name = models.CharField(max_length=20, null=True)
	#SUBJECT
	subject = models.TextField(max_length=20, null=True)
	#BODY
	body = models.TextField(max_length=20, null=True)
	date = models.DateTimeField(auto_now=True, null=True)

	russel = (('male', 'gender'),('female','gender'))
	gender = models.CharField( max_length=10, choices=russel, default='none')


	def __str__(self):
		return self.name



	#kapag meron babaguhin sa manage.py(server)
	# python manage.py makemigrations
	# python manage.py migrate
	# coverage run manage.py test
	# coverage report
	# python manage.py test app
	# coverage html
