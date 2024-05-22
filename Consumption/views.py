from django.shortcuts import render
from UnitCalculator.models import SudoBillModel
from Authentication.models import UserDevices
from .form import Bill


def bill(request):
    if request.method == 'POST':
        form = Bill(user=request.user, data=request.POST)
        if form.is_valid():
            selected_bill_id = form.cleaned_data['selected_bill']
            print(selected_bill_id)
            invoice_response = Invoice(request, selected_bill_id)
            return invoice_response

    else:
        form = Bill(user=request.user)
    return render(request, 'Consumption/bill.html', {'form': form})


def Invoice(request, bill_id):
    device_list = []  # devicesNAme
    consumption_list = []  # totalTimeDeviceRUNNING
    watt_list = []  # DEVICE WAttage
    device_comsumption = []  # Power Consumption (kWh)
    perDevicePrice = []  # perdevicePrice
    totalDaily = 0
    dy_data = bill_id.dynamic_data
    for device, consumption in dy_data['device_dic'].items():
        device_list.append(device)
        consumption_list.append(consumption)
    wattage_values = UserDevices.objects.filter(
        DeviceName__in=device_list, author=request.user).values_list('Watt', flat=True)

    for watt in wattage_values:
        watt_list.append(watt)

    for consumption, watt in zip(consumption_list, watt_list):
        device_comsumption.append((watt / 1000) * consumption)

    for i in range(len(device_comsumption)):
        perDevicePrice.append(device_comsumption[i]*10)

    totalDaily = sum(perDevicePrice)
    print(totalDaily)
    totalMonthly = totalDaily*30
    totalyearly = totalDaily*365

    length = len(device_list)
    return render(request, 'Consumption/Invoice.html', {'device_list': device_list,
                                                        'consumption_list': consumption_list,
                                                        'watt_list': watt_list,
                                                        'device_comsumption': device_comsumption,
                                                        'perDevicePrice': perDevicePrice,
                                                        'totalDaily': totalDaily,
                                                        'totalMonthly': totalMonthly,
                                                        'totalyearly': totalyearly,
                                                        'length': length})
