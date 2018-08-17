from rest_framework import permissions;
import api
import pdb

class DetailPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("hasown")
        if request.user.is_superuser:
            return True
        if obj.account == request.user:
            return True
        if request.method in permissions.SAFE_METHODS:
            return hasattr(request.user, 'company')
        return False


class ListPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if hasattr(request.user, 'company'):
            return True
        return False

class AlterPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.account == request.user:
            return True
        return False
