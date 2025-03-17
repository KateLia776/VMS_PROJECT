from django.shortcuts import render, redirect, get_object_or_404
from .models import VehicleInfo

def vehicles_view(request):
    vehicles = VehicleInfo.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})

def add_vehicle(request):
    if request.method == "POST":
        VehicleInfo.objects.create(
            VIN=request.POST['VIN'],
            vehicle_make_model=request.POST['vehicle_make_model'],
            body_colour=request.POST['body_colour'],
            plate_number=request.POST['plate_number'],
            registration_cert_number=request.POST['registration_cert_number']
        )
        return redirect('vehicles')

    return render(request, 'add_vehicle.html')

def edit_vehicle(request, vin):
    vehicle = get_object_or_404(VehicleInfo, VIN=vin)

    if request.method == "POST":
        vehicle.vehicle_make_model = request.POST['vehicle_make_model']
        vehicle.body_colour = request.POST['body_colour']
        vehicle.plate_number = request.POST['plate_number']
        vehicle.registration_cert_number = request.POST['registration_cert_number']
        vehicle.save()
        return redirect('vehicles')

    return render(request, 'add_vehicle.html', {'vehicle': vehicle})
