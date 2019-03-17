from django.urls import path 
from . import views 

urlpatterns = [ 
	
	path('', views.home, name='mainapp-home'), 
	path('about', views.about, name='about-page'),

] 