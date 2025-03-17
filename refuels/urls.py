from django.urls import path
from .views import refuels_view, add_refuel, edit_refuel  # Import views to use later

urlpatterns = [
    path('', refuels_view, name='refuels'),  # Naming the path
    path('add/', add_refuel, name='add_refuel'),  # Add a new refuel
    path('edit/<int:refuel_id>/', edit_refuel, name='edit_refuel'),  # Edit an existing refuel
]