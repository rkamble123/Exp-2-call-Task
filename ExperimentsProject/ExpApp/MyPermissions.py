from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" and request.user.is_authenticated:
            return True
        elif  (request.method == "GET" or request.method == "POST" or request.method == "PUT" or request.method == "PATCH" or request.method == "DELETE") and request.user == 'admin'  :
            return True
        else:
            return False