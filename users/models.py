from django.db import models
from django.contrib.auth.models import User
from PIL import Image #Import Pillow stuff to save 

#This class lets you create Profiles, with pictures associated with them. You need to create this Profile class because the default Django User class doesn't come with pictures.
#Don't forget to add the class to the admin.py file of this folder.
class Profile(models.Model):
	#Note that the below won't work if you write the class User with quotes.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#upload_to specifies the directory that images get uploaded to
	#You need to install Pillow to use the ImageField. It's a library for working with images in Python. Download it with "pip install Pillow"
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	#We're overriding the save method for pictures, because we want to restrict their size
	#This save method is a method that alrady exists in our parent class, but we're creating our own
	#Note that there are many different ways of accomplishing this same goal of resizing pics.
	def save(self, *args, **kwargs):
		#Run the save method of our parent class
		super(Profile, self).save(*args, **kwargs)

		#Grab the saved image and resize it. The Image object is imported from PIL
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			#This is a tuple of the max sizes that we want
			output_size = (300, 300)
			#Resize the image
			img.thumbnail(output_size)
			#Save image to the same path
			img.save(self.image.path)


