from django.shortcuts import render, get_object_or_404, redirect

from .models import User
from .forms import UserForm

def users_list(request):
  users = User.objects.all()
  return render(request, "users/users_list.html", {"users": users})
  