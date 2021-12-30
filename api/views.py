from django.shortcuts import render
from rest_framework import generics
from recipie.serializers import RecipieSerializer
from recipie.models import Recipie

# Create your views here.
class RecipieListView(generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer
    search_fields= ['name']

class RecipieDetailView(generics.RetrieveAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer