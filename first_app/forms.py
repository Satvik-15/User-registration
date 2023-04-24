from django.forms import ModelForm
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        # Here we can also use include() or exclude() for pertucular files.
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = '__all__'
