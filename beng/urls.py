from django.urls import path
from . import views

urlpatterns = [
	path('', views.mainpage, name="home"),
	path('goods', views.Patient, name="goods"),
	path('bank', views.Donor, name="bank"),
	path('request', views.request, name="request"),
	path('about', views.about, name="about")
]

