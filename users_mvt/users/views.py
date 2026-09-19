from django.shortcuts import render, get_object_or_404, redirect

from .models import User
from .forms import UserForm

def users_list(request):
  users = User.objects.all()
  return render(request, "users/users_list.html", {"users": users})

def user_detail(request, id):
  user = get_object_or_404(User, id=id)
  return render(request, "users/user_detail.html", {"user": user})

def user_create(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, "users/user_detail.html", {"user": form.instance})
  else:
    form = UserForm()
  return render(request, "users/user_form.html", {'form': form})