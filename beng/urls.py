from django.urls import path
from . import views

urlpatterns = [
	path('', views.Russex),
	path('goods/', views.Page),
]
