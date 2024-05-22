from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Authentication.models import UserDevices


class DeviceForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        devices = UserDevices.objects.filter(author=user)

        for device in devices:
            field_name = f"device_{device.id}"
            self.fields[field_name] = forms.IntegerField(
                label=device.DeviceName)
