from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDevices


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    adress = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "adress",
                  "phone_number", "password1", "password2"]


class UserDeviceFrom(forms.ModelForm):
    class Meta:
        model = UserDevices
        fields = ["DeviceName", "manufacturer", "Model", "Watt"]
