from django.shortcuts import render, redirect, get_object_or_404
from .models import DriverInfo

# Create your views here.

def drivers_view(request):
    drivers = DriverInfo.objects.all()
    return render(request, 'drivers.html', {'drivers': drivers})

def add_driver(request):
    if request.method == "POST":
        DriverInfo.objects.create(
            name=request.POST['name'],
            lastname=request.POST['lastname'],
            birthday=request.POST['birthday'],
            drivers_license_number=request.POST['drivers_license_number'],
            drivers_license_issue_date=request.POST['drivers_license_issue_date'],
            drivers_license_expiry_date=request.POST['drivers_license_expiry_date'],
            employment_date=request.POST['employment_date'],
            email=request.POST['email']
        )
        return redirect('drivers')

    return render(request, 'add_driver.html')

def edit_driver(request, driver_id):
    driver = get_object_or_404(DriverInfo, id=driver_id)

    if request.method == "POST":
        driver.name = request.POST['name']
        driver.lastname = request.POST['lastname']
        driver.birthday = request.POST['birthday']
        driver.drivers_license_number = request.POST['drivers_license_number']
        driver.drivers_license_issue_date = request.POST['drivers_license_issue_date']
        driver.drivers_license_expiry_date = request.POST['drivers_license_expiry_date']
        driver.employment_date = request.POST['employment_date']
        driver.email = request.POST['email']
        driver.save()
        return redirect('drivers')

    return render(request, 'add_driver.html', {'driver': driver})
