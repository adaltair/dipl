from django.shortcuts import get_object_or_404
from rest_framework import viewsets,  permissions, status
from rest_framework.response import Response
from rest_framework import generics
from .models import App
from .serializers import AppSerializer
from rest_framework.permissions import *


# LIST
class AppListView(generics.ListAPIView):
    serializer_class = AppSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        query = App.objects.all()
        return query
    
# CREATE
class AppCreateView(generics.CreateAPIView):
    serializer_class = AppSerializer
    
    def perform_create(self, serializer):
        # Automatically set the user field to the current user on create
        serializer.save(user=self.request.user)
        
# UPDATE
class AppUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    
    def update(self, request, *args, **kwargs):
        # Ensure the user remains the same when updating
        app_instance = self.get_object()
        if app_instance.user != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

# DELETE
class AppDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = AppSerializer
    queryset = App.objects.all()

    def destroy(self, request, *args, **kwargs):
        # Ensure the user remains the same when deleting
        app_instance = self.get_object()
        if app_instance.user != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


# class AppRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    
    
#     queryset = App.objects.all()
#     serializer_class = AppSerializer

#     def update(self, request, *args, **kwargs):
#         # Ensure the user remains the same when updating
#         app_instance = self.get_object()
#         if app_instance.user != request.user:
#             return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
#         return super().update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         # Ensure the user remains the same when deleting
#         app_instance = self.get_object()
#         if app_instance.user != request.user:
#             return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
#         return super().destroy(request, *args, **kwargs)


