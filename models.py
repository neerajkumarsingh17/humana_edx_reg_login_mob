from django.db import models
from django.conf import settings
from django.forms import ModelForm


class User(models.Model):
    # Backwards compatible settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    moblie_number = models.CharField(max_length=10, blank=False, unique=True, null=False)

    def __str__(self):
        return 'User Name - %s  and  Mobile Number - %s' % (self.user, self.moblie_number)

