from django.db import models

# BLOODTYPE_CHOICES = [('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),]

class Login(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50) 
    def __str__(self):
    	return self.username

class Patient(models.Model):
	usser = models.ForeignKey(Login, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	contactNumber = models.CharField(max_length=20)
	gendr = models.CharField(max_length=10)
	age = models.IntegerField()
	male=(('male', 'MALE'), ('female', 'FEMALE'))
	female =models.CharField(max_length=10, choices=male, default='none')
	def __str__(self):
		return self.firstName

class Donor(models.Model):
	usser = models.ForeignKey(Login, on_delete=models.CASCADE)

	addess = models.CharField(max_length=100)
	donrBloodType=(('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'))
	gnder = models.CharField(max_length=10, choices=donrBloodType, default='none')
	def __str__(self):	
		return self.Donor

class RequestDonor(models.Model):
	usser= models.ForeignKey(Login, on_delete=models.CASCADE)
	requestDonorID = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200)
	donorBloodType=(('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'))
	gender = models.CharField(max_length=10, choices=donorBloodType, default='none')
	def __str__(self):	
		return self.requestDonorID

class RequestOrganizer(models.Model):
	usser = models.ForeignKey(Login, on_delete=models.CASCADE)
	requestOrganizerID = models.AutoField(primary_key=True)
	hospitalName = models.CharField(max_length=100)
	hospitalAddress = models.CharField(max_length=100)
	businessEmail = models.EmailField(max_length=100)
	def __str__(self):
		return self.requestOrganizerID



# class Usseerr(models.Model):
# 	pass

# class Item(models.Model):
	
# 	students = models.ForeignKey(Usseerr, default=None, on_delete=models.CASCADE, null=True)
# 	#SECTION
# 	name = modelsfrom django.db import models

# Create your models here.

#GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
# 	#SUBJECT
# 	subject = models.TextField(max_length=20, null=True)
# 	#BODY
# 	body = models.TextField(max_length=20, null=True)
# 	date = models.DateTimeField(auto_now_add=True, null=True)

# 	russel = (('male', 'gender'),('female','gender'))
# 	gender = models.CharField( max_length=10, choices=russel, default='none')


# 	def __str__(self):
# 		return self.name



	#kapag meron babaguhin sa manage.py(server)
	# python manage.py makemigrations
	# python manage.py migrate
	# coverage run manage.py test
	# coverage report
	# python manage.py test app
	# coverage html




	#kapag meron babaguhin sa manage.py(server)
	# python manage.py makemigrations
	# python manage.py migrate
	# coverage run manage.py test
	# coverage report
	# python manage.py test app
	# coverage html
