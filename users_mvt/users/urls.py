from django.urls import path
from .views import *

urlpatterns = [
  path("", users_list, name="users_list"),
  path("users/<int:id>", user_detail, name="user_detail"),
  path("users/create", user_create, name="user_create"),
  path("users/update/<int:id>", user_update, name="user_update"),
  path("users/delete/<int:id>", user_delete, name="user_delete")
]