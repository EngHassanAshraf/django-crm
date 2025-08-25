from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm


def register_logic(request):
    user_data = RegisterForm(request.POST)
    if user_data.is_valid():
        try:
            user = user_data.save()
            login(request, user)
            messages.success(
                request, f"Welcome, {user_data.cleaned_data["first_name"]}"
            )
            return redirect("home")
        except Exception as e:
            print("ex")
            messages.error(request, f"{e}")
            return redirect("register/")

    return redirect("register/")


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
        if "register" in request.path:
            register_logic(request)
        else:
            login_logic(request)

    if "register" in request.path:
        return render(request, "home.html", {"register_form": RegisterForm()})
    else:
        return render(request, "home.html")


def ulogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged Out")
    return redirect("home")
