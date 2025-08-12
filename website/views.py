from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_logic(request):
    pass


def login_logic(request):
    email = request.POST.get("email").split("@")[0]
    password = request.POST.get("password")
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        messages.success(request, "Logged In")
        return redirect("home")
    else:
        messages.error(request, "Login Failed")
        return redirect("home")


def home(request):
    if "register" in request.path and request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        if "regsiter" in request.path:
            register_logic(request)
            return redirect("home")
        else:
            login_logic(request)

    if "register" in request.path:
        return render(request, "home.html", {"register_form": "form"})
    else:
        return render(request, "home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        pass

    return render(request, "auth/register.html", {})


def ulogin(request):
    pass


def ulogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged Out")
    return redirect("home")
