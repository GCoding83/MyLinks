#This is a signal that gets fired after an object is saved
#We're using this so that a profile gets automatically created every time a user creates an account
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#The User model is the "sender" of the signal, since it is what is sending the signal; and we need a 'receiver', which is a function that gets this signal and then functions the task.
from django.dispatch import receiver
from .models import Profile

#The decorator means: when the user is saved, send the "post_save" signal. This signal is then received by the "create_profile" function
@receiver(post_save, sender=User)#
#"**kwargs" is simply something that lets you add additional arguments to a function.
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


#Now, we make sure that the profile gets saved authomatically when created.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()