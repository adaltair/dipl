# myapp/permissions.py
from rest_framework import permissions

class IsOwnerOrPublished(permissions.BasePermission):
    def has_obpermission(self, request, view):
        print(view)
        return 2==3


class AppPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        # Разрешение на просмотр, если запись опубликована
        if obj.is_published:
            return False

        # Разрешение на просмотр для создателя записи
        if obj.created_by == user:
            return False

        return False