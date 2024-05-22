from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from Authentication.models import UserDevices
from .forms import DeviceForm
from .models import SudoBillModel
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/login")
def device_form_view(request):
    list1 = []
    list2 = []
    list3 = []
    dic1 = {}
    total = 0
    divce_dic = {}
    devices = UserDevices.objects.filter(author=request.user)

    if request.method == 'POST':
        form = DeviceForm(request.user, request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            for device in devices:
                field_name = f"device_{device.id}"
                dic1[device.id] = device.DeviceName
            for device in devices:
                field_name = f"device_{device.id}"
                field_value = cleaned_data.get(field_name)
                list2.append(field_value)
                total = sum(list2)

            list3 = list(dic1.values())
            for i in range(len(list3)):
                divce_dic[list3[i]] = list2[i]

            sudo_bill = SudoBillModel(
                author=request.user,
                totalAmount=total,
                dynamic_data={
                    "device_dic": divce_dic,
                }
            )
            sudo_bill.save()

    else:
        form = DeviceForm(request.user)

    return render(request, 'UnitCalculator/sudobill.html', {'form': form})
