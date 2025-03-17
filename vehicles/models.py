from django.db import models

class VehicleInfo(models.Model):
    VIN = models.CharField(max_length=50, primary_key=True)
    vehicle_make_model = models.CharField(max_length=50)
    body_colour = models.CharField(max_length=20)
    plate_number = models.CharField(max_length=20, unique=True)
    registration_cert_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.vehicle_make_model} ({self.plate_number})"
