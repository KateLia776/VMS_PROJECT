from django.shortcuts import render, redirect, get_object_or_404
from .models import Refuel
from vehicles.models import VehicleInfo
from drivers.models import DriverInfo

# Create your views here.

def refuels_view(request):
    refuels = Refuel.objects.select_related('driver_id', 'vehicle_vin').order_by('refuel_id')
    return render(request, 'refuels.html', {'refuels': refuels})

def add_refuel(request):
    if request.method == "POST":
        Refuel.objects.create(
            vehicle_vin=VehicleInfo.objects.get(VIN=request.POST['vehicle_vin']),
            driver_id=DriverInfo.objects.get(id=request.POST['driver_id']),
            mileage_at_refuel=request.POST['mileage_at_refuel'],
            fuel_liters=request.POST['fuel_liters'],
            refuel_date=request.POST['refuel_date']
        )
        return redirect('refuels')

    return render(request, 'add_refuel.html', {
        'vehicles': VehicleInfo.objects.all(),
        'drivers': DriverInfo.objects.all()
    })

def edit_refuel(request, refuel_id):
    refuel = get_object_or_404(Refuel, refuel_id=refuel_id)

    if request.method == "POST":
        refuel.vehicle_vin = VehicleInfo.objects.get(VIN=request.POST['vehicle_vin'])
        refuel.driver_id = DriverInfo.objects.get(id=request.POST['driver_id'])
        refuel.mileage_at_refuel = request.POST['mileage_at_refuel']
        refuel.fuel_liters = request.POST['fuel_liters']
        refuel.refuel_date = request.POST['refuel_date']
        refuel.save()
        return redirect('refuels')

    return render(request, 'add_refuel.html', {
        'refuel': refuel,
        'vehicles': VehicleInfo.objects.all(),
        'drivers': DriverInfo.objects.all()
    })
