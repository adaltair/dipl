from django.shortcuts import get_object_or_404
from rest_framework import viewsets,  permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.views import APIView
from .models import App
from .serializers import AppSerializer
from .permissions import IsOwnerOrPublished, AppPermission
from rest_framework.permissions import *
from django.db.models import Q

class AppView(viewsets.ViewSet):
    """
    A simple Viewset for viewing all product
    """
    queryset = App.objects.all()

    @extend_schema(responses=AppSerializer)
    def list(self, request):
        serializer = AppSerializer(self.queryset, many=True)
        return Response(serializer.data)



class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.created_by == request.user


# filter(App(is_published=True) | App(created_by = request.user.id)), many=True)

class AppListView(generics.ListCreateAPIView):
    serializer_class = AppSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        query = App.objects.filter(Q(created_by=user) | Q(is_published=True))
        return query
    
    def perform_create(self, serializer):
        # Automatically set the user field to the current user on create
        serializer.save(user=self.request.user)

class AppRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [PostUserWritePermission]
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def update(self, request, *args, **kwargs):
        # Ensure the user remains the same when updating
        app_instance = self.get_object()
        if app_instance.user != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Ensure the user remains the same when deleting
        app_instance = self.get_object()
        if app_instance.user != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
