from rest_framework import generics
from rest_framework import mixins
from back.serializers import TourSerializer, AboutSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from back.models import Tour, About
from django.shortcuts import Http404


class TourListAPIView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class AboutListAPIView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
