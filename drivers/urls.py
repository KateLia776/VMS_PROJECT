from django.urls import path
from .views import drivers_view, add_driver, edit_driver  # Import views

urlpatterns = [
    path('', drivers_view, name='drivers'), # Naming the path
    path('add/', add_driver, name='add_driver'),  # Add a new driver
    path('edit/<int:driver_id>/', edit_driver, name='edit_driver'),  # Edit an existing driver
]