#Note that we don't need to create this file to use the Django built-in forms.
#...We create this file only if we want to modify the built-in forms - for inst, to add an email field in the form.

#******Be sure to install Django Crispy (pip install django-crispy-forms) and add it to your list of installed apps in settings.py. This app lets you add nice, bootstrap-type styles to Django forms. Note that we also added a spec. for Crispy at the very bottom of our settings.py file.


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#The class we're creating inherits from the built-in form, and it just adds to it.
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	#The Meta class lets us specify all the configurations in one place
	class Meta:
		#The model that is affected by our changes is the User model
		model = User
		#The fields that we want in the form, and their order
		fields = ['username', 'email', 'password1', 'password2']


#We create a "model form", which is a form that works with a specific database model. In this case, it's a form that updates our User model
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	#The Meta class lets us specify all the configurations in one place
	class Meta:
		#The model that is affected by our changes is the User model
		model = User
		#This lets our form know that we want to work with the username and email
		fields = ['username', 'email']

#Lets the user update their profile picture
class ProfileUpdateForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ['image']



