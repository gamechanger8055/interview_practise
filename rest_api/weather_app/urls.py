from django.urls import path
from .views import WeatherApiView
#from rest_framework.urls import urlpatterns

urlpatterns = [
    path("weather/", WeatherApiView.as_view(), name="weather")
]
