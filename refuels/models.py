from django.db import models
from vehicles.models import VehicleInfo
from drivers.models import DriverInfo

# Create your models here.

class Refuel(models.Model):
    refuel_id = models.AutoField(primary_key=True)
    vehicle_vin = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE, to_field='VIN', db_column='vehicle_vin')
    driver_id = models.ForeignKey(DriverInfo, on_delete=models.CASCADE, db_column='driver_id')
    mileage_at_refuel = models.IntegerField()
    fuel_liters = models.FloatField()
    refuel_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refuel {self.refuel_id} - {self.vehicle_vin} by {self.driver_id}"
