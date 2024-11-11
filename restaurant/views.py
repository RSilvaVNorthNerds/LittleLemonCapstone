from django.shortcuts import render
from .models import Booking, Menu
from rest_framework import viewsets
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
