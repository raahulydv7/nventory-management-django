from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.contrib.auth import login
from django.contrib import messages
from .decorators import admin_required,staff_required,login_required_custom

@admin_required
def register_user(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User registerd successfully!")
        else:
            messages.error(request, 'Unalbe to register user , Try again.')
    else:
        form = UserForm()
    return render(request, 'accounts/user_register.html',{'form':form})




@login_required_custom
def home(request):
    return render(request, 'home.html')
