from django.urls import path
from .views import user_login, user_register

urlpatterns = [
    path("", user_login, name="user_login"),
    path("register/", user_register, name="user_register"),
]
