from django.contrib import admin
from .models import Login, Patient, Donor, RequestDonor, RequestOrganizer
# Register your models here.
admin.site.register(Login)
admin.site.register(Patient)
admin.site.register(Donor)
admin.site.register(RequestDonor)
admin.site.register(RequestOrganizer)