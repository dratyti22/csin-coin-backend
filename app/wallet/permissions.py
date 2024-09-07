from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreateIsAdminOrRead(BasePermission):

    """
    смотреть все
    создавать только админ
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated and request.user.is_staff
