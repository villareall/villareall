from django.urls import path
from . import views

urlpatterns = [
	path('', views.mainpage),
	path('goods', views.Patient, name="goods"),
	path('goods', views.Donor, name="goods")
]
