from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CarDetailSerializer, CarsListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
