from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Разрешение для доступа только активным пользователям."""
    message = "Доступ разрешен только активным пользователям."

    def has_permission(self, request, view):
        return request.user.is_active


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка прав доступа пользователя к профилю"""
    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.email
