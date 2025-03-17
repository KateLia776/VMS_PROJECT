from django.urls import path
from .views import trips_view, add_trip, edit_trip  # Import views

urlpatterns = [
    path('', trips_view, name='trips'), # Naming the path
    path('add/', add_trip, name='add_trip'),  #Add new trip
    path('edit/<int:trip_id>/', edit_trip, name='edit_trip'),  # Edit existing trip
]