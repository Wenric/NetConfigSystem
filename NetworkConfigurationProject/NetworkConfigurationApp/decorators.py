from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib.auth.models import Group

def role_required(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []
    
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not allowed to access this page")
            
            user_groups = request.user.groups.values_list('name', flat=True)
            user_groups = [group.lower() for group in user_groups]  # Convert to lowercase
            allowed_roles_lower = [role.lower() for role in allowed_roles]  # Convert to lowercase
            
            print(f"User: {request.user.username}, Groups: {list(user_groups)}, Allowed Roles: {allowed_roles_lower}")  # Debugging line
            if not any(role in user_groups for role in allowed_roles_lower):
                return HttpResponseForbidden("You are not allowed to access this page")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
