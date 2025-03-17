from django.urls import path
from .views import main_view  # Import views

urlpatterns = [
    path('', main_view, name='main'),  # Naming the path
]