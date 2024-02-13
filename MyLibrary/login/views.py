from django.shortcuts import render

# rest_framework imports
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from database.models import UserProfile


@csrf_exempt
@api_view(["POST", "GET"])
def user_login(request):

    if request.method == "POST":

        email = request.data.get("email")
        password = request.data.get("password")

        if UserProfile.objects.filter(email=email, password=password).exists():
            data = {"username": request.data.get("email")}

            return render(request, "index.html", data)
            # return Response("User successfully logged in")
        else:
            pass
            # return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)

    return render(request, "login.html")


@csrf_exempt
@api_view(["POST", "GET", "PUT"])
def user_register(request):

    if request.method == "POST":

        UserProfile.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            phone=request.data["phone"],
            password=request.data["password"],
        )

        return Response("user successfully registerred")

    return render(request, "register.html")
