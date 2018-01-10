from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Edicao do propio UserProfile"""
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile == request.user.id
