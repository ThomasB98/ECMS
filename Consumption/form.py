from django import forms
from django.contrib.auth.models import User
from Authentication.models import UserDevices
from UnitCalculator.models import SudoBillModel


class Bill(forms.Form):
    selected_bill = forms.ModelChoiceField(
        queryset=None,
        empty_label="Select a bill"
    )

    def __init__(self, user, *args, **kwargs):
        super(Bill, self).__init__(*args, **kwargs)
        self.user = user
        if user:
            self.fields['selected_bill'].queryset = SudoBillModel.objects.filter(
                author=user)
