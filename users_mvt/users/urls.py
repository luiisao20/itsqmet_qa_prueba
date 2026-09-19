from django.urls import path
from .views import *

urlpatterns = [
  path("", users_list, name="users_list"),
  # path("product/<int:id>", product_detail, name="product_detail"),
  # path("product/create", product_create, name="product_create"),
  # path("product/update/<int:id>", product_update, name="product_update"),
  # path("product/delete/<int:id>", product_delete, name="product_delete")
]