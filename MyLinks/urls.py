"""MyLinks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#The two imports below are for user images
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
#I import the "incluce" function, which specifies which routes go to our (specif) app URLs

#To have acces to views like Login and Logout already developed by Django
from django.contrib.auth import views as auth_views

from django.urls import path, include

#Import the Users app for registration and login
#We're importing it under a different name just to avoid possible confusion
from users import views as user_views



urlpatterns = [
    #This maps the URL blog (as aur main page) to the function included in the file "urls" inside our "blog" directory
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    #The two below (Login and Logout) are class-based views. Django handles the logic and forms (etc.), but not the templates.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('my_projects/', include('users.urls')),
    path('profile/', user_views.profile, name='profile'),    
    path('register/', user_views.register, name='register'),
]

#The blow is the route for our media (ex: profile pics). We could put it inside the urlpatterns list, but it's better 
#to separate it, because this path works only when we're in development mode (and not production mode), so we want to distinguish this route from the others.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

