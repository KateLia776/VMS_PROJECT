from django.urls import path
from .views import vehicles_view, add_vehicle, edit_vehicle  # Import views

urlpatterns = [
    path('', vehicles_view, name='vehicles'),  # Naming a path
    path('add/', add_vehicle, name='add_vehicle'),  # Add a new vehicle
    path('edit/<str:vin>/', edit_vehicle, name='edit_vehicle'),  # Edit an existing vehicle
]
