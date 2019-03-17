from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #This function imports signals, which save any new profile that gets created.
    def ready(self):
    	import users.signals
