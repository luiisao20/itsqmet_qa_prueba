from django.urls import path
from .views import *

urlpatterns = [
  path("", users_list, name="users_list"),
  path("users/<int:id>", user_detail, name="user_detail"),
  path("users/create", user_create, name="user_create"),
  # path("product/update/<int:id>", product_update, name="product_update"),
  # path("product/delete/<int:id>", product_delete, name="product_delete")
]