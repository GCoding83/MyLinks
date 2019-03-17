from django.shortcuts import render, redirect

#NOTE: Usually, we would import the blow module, which is the default Django buil-in form. But we modified this default form in our forms.py file, so we don't need to import the default one.
#from django.contrib.auth.forms import UserCreationForm

#For flash messages we'll be sending users ater they fill out the form
#...Possible messages are: messages.debug, messages.info, messages.success, messages.warning, messages.error
from django.contrib import messages

#To access a page like Profile, one needs to be logged in.
from django.contrib.auth.decorators import login_required

#We're importing the modification to the built-in form that we created in forms.py 
#We're also importing the forms we created for updating user info
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

#Django has built-in classes for registration that automaically get converted into HTML forms!
#Note that the urls.py file (from our users GLobal Project folder) runs the below function for any user that enters the ".../register" route. 
#...We then handle the user's entry in two ways: if it was accessed via the URL, then it's a GET reqiest that returns an empty form.
#...However, if it was accessed after the user submitted the form, then it's a POST request, and it needs to return a filled out form (with the request.POST data)
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#Make sure that the data we're receiving is valid.
		if form.is_valid():
			#Save user
			form.save()
			username = form.cleaned_data.get('username')
			#Return success message
			messages.success(request, f'Account created for {username}!')
			#Return user to the home page if successful (the name "mainapp-home" is the one we assigned to our home page in the url pattern (of mainapp folder))
			return redirect('mainapp-home')

	#If the request is not a POST, it will just render an empty form
	else:
		form = UserRegisterForm()
	#The dictionary is where you specify the context to that template (Which lets us access the form within that template)
	return render(request, 'users/register.html', {'form': form})

#The decorator requires being logged in to access the Profile page
@login_required
def profile(request):
	#Make sure this info is submitted through the form (i.e. POST)
	if request.method == 'POST':
		#The u_form and p_form variables are associated with the forms we created for the user to update their profile info
		#Including the instance argument makes it so that the update forms will already be populated with the user's current info.
		#The request.POST stuff (and .FILES) is some requires HTTP stuff...
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
									request.FILES, 
									instance=request.user.profile)
		#The new data gets saved only if it's valid
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			#Return user to the home page if successful (the name "mainapp-home" is the one we assigned to our home page in the url pattern (of mainapp folder))
			return redirect('profile')


	else:
		#The u_form and p_form variables are associated with the forms we created for the user to update their profile info
		#Including the instance argument makes it so that the update forms will already be populated with the user's current info.
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

@login_required
def my_projects(request):
	return render(request, 'users/my_projects.html')
