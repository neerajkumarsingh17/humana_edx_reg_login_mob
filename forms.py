from django.forms import ModelForm
from .models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(ModelForm):
   
    class Meta:
        model = User
        fields = ('moblie_number',)
        labels = {
            'moblie_number': _('Moblie Number'),
        },