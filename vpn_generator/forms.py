from django.forms import ModelForm ,ValidationError
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)
