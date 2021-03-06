from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

def validate_email(value):
    if User.objects.filter(email= value).exists():
        raise ValidationError((f'{value} is register already'), params={'value':value})

class UserForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

