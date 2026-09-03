from rest_framework.permissions import BasePermission


class CheckStatus(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'pro'


class CheckMovie(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.status == 'pro':
            return True
        elif request.user.status == 'simple' and obj.movie_status == 'simple':
            return True
        return False