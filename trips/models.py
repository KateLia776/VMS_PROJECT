from django.db import models
from django.utils import timezone
from vehicles.models import VehicleInfo
from drivers.models import DriverInfo

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    vehicle_vin = models.ForeignKey(
        VehicleInfo, on_delete=models.CASCADE, to_field='VIN', db_column='vehicle_vin'
    )
    driver_id = models.ForeignKey(
        DriverInfo, on_delete=models.CASCADE, db_column='driver_id'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    start_mileage = models.IntegerField(null=True, blank=True, default=None)
    end_mileage = models.IntegerField(null=True, blank=True, default=None)
    start_time = models.TimeField(null=True, blank=True, default=None)
    end_time = models.TimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Trip {self.trip_id}: {self.from_location} → {self.to_location}"
