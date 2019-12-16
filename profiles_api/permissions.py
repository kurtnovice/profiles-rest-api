from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        #returns true only if the user wants to update HISOWN PROFILE

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update thier own status"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

class ViewOwnStatus(permissions.BasePermission):
    """Only allow owner of status to view status"""
    def has_object_permission(self, request, view, obj):
        return obj.user_profile.id == request.user.id
