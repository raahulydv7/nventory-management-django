from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def login_required_custom(view_func):
    """
    Ensures that the user is logged in.
    If not, redirects to login page with an error message.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to continue.")
            return redirect('login') 
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    """
    Restricts access to only users with the ADMIN role.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'ADMIN':
            messages.error(request, "You are not authorized to access this page.")
            return redirect('home')  
        return view_func(request, *args, **kwargs)
    return wrapper


def staff_required(view_func):
    """
    Restricts access to only users with the STAFF role.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'STAFF':
            messages.error(request, "Staff access only.")
            return redirect('home')  
        return view_func(request, *args, **kwargs)
    return wrapper
