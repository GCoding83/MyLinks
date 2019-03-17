from django.urls import path
from . import views


urlpatterns = [
    #First argument is the url; second argument is the location of the function associated with the url, i.e. the function that (e.g.) gets the HTML file; the third argument is the name of this route.
    path('', views.home, name='blog-home'),
]
