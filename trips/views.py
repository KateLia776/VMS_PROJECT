from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from vehicles.models import VehicleInfo
from drivers.models import DriverInfo

# Create your views here.

def trips_view(request):
    trips = Trip.objects.all()
    return render(request, 'trips.html', {'trips': trips})

def add_trip(request):
    if request.method == "POST":
        selected_vin = request.POST['vehicle_vin']
        Trip.objects.create(
            vehicle_vin=VehicleInfo.objects.get(VIN=selected_vin),
            driver_id=DriverInfo.objects.get(id=request.POST['driver_id']),
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            from_location=request.POST['from_location'],
            to_location=request.POST['to_location'],
            start_mileage=request.POST['start_mileage'],
            end_mileage=request.POST.get('end_mileage', None),
            start_time=request.POST.get('start_time', None),
            end_time=request.POST.get('end_time', None)
        )
        return redirect('trips')

    trips = Trip.objects.all()
    vehicles = VehicleInfo.objects.all()
    drivers = DriverInfo.objects.all()
    return render(request, 'add_trip.html', {'trips': trips, 'vehicles': vehicles, 'drivers': drivers})


def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, trip_id=trip_id)

    if request.method == "POST":
        trip.vehicle_vin = VehicleInfo.objects.get(VIN=request.POST['vehicle_vin'])
        trip.driver_id = DriverInfo.objects.get(id=request.POST['driver_id'])
        trip.start_date = request.POST.get('start_date', None)
        trip.end_date = request.POST['end_date']
        trip.from_location = request.POST['from_location']
        trip.to_location = request.POST['to_location']
        trip.start_mileage = request.POST['start_mileage']
        trip.end_mileage = request.POST.get('end_mileage', None)
        trip.start_time = request.POST.get('start_time', None) or None
        trip.end_time = request.POST.get('end_time', None) or None
        trip.save()
        return redirect('trips')

    return render(request, 'add_trip.html',
                  {'trip': trip, 'vehicles': VehicleInfo.objects.all(), 'drivers': DriverInfo.objects.all()})