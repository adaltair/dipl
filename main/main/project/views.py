from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import generics
# Create your views here.
from .models import App
from .serializers import AppSerializer


class AppView(viewsets.ViewSet):
    """
    A simple Viewset for viewing all product
    """
    
    queryset = App.objects.all()
    
    @extend_schema(responses=AppSerializer)
    def list(self, request):
        serializer = AppSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class AppListCreate(generics.ListCreateAPIView):
    queryset = App.objects.all()
    
    serializer_class = AppSerializer
    
class AppRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer