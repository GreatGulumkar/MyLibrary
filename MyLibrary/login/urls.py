from django.urls import path
from .views import user_login, user_register, user_logout

urlpatterns = [
    path("", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),  
    path("register/", user_register, name="user_register"),
]
