from django.shortcuts import render
#from rest_framework import
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class WeatherApiView(APIView):
    def get(self,request):
        latitude=request.GET.get('lat')
        longitude=request.GET.get('lon')
        api_id="123assdwed"
        if not longitude or not latitude or not api_id:
            return Response("Please pass the correct credentials",400)
        uri='https://api.openweathermap.org/data/2.5/weather?lat='+str(latitude)+'&lon='+str(longitude)+"&appid="+api_id
        response=requests.get(uri)
        if response.status_code==200:
            data=response.json()
            return Response(data)


