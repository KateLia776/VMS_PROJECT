from django.db import models

# Create your models here.

class DriverInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    birthday = models.DateField()
    drivers_license_number = models.CharField(max_length=20, unique=True)
    drivers_license_issue_date = models.DateField(null=True, blank=True)
    drivers_license_expiry_date = models.DateField(null=True, blank=True)
    employment_date = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.email})"