from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UnitCalculator.models import SudoBillModel
# Create your views here.


@login_required(login_url="/Authentication/login")
def dashboard(request):
    bills = SudoBillModel.objects.filter(author=request.user)

    return render(request, 'Dashboard/dashboard.html', {"bills": bills})
