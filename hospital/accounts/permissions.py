from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404


class IsSuperUser(permissions.BasePermission):
    """If user is super user"""

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsOwner(permissions.BasePermission):
    """
    Check if the user is the owner of the resource specified in the URL.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.user == request.user
        else:
            return False


class AllowListStaffOnlyCreateUpdate(permissions.BasePermission):
    """
    - This allows the list method for all authenticated users but not other methods
    - Allows create, update, patch on other methods for upseruser and staff

    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if view.action in ["update", "partial_update", "destroy", "create"]:
                if request.user.is_staff or request.user.is_superuser:
                    return True
                else:
                    return False
            else:
                return True

        return False


class ListOnlyForStaffUser(permissions.BasePermission):
    """
    - This allows the list method for only staff users.
    - Allows create, update, patch on other methods for authenticated users
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if view.action == "list" and (
                request.user.is_staff or request.user.is_superuser
            ):
                return True

            return False
        return False


class IsStaff(permissions.BasePermission):
    """
    User is staff or admin
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_staff or request.user.is_superuser


class IsDeveloper(permissions.BasePermission):
    """
    Check if user is a developer and can access the documentation.
    """

    def has_permission(self, request, view):
        """_summary_: Check if user is authenticated."""

        return request.user.is_authenticated and request.user.is_developer
