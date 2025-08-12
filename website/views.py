from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == "POST":
        email = request.POST.get("email").split("@")[0]
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "LoggedIn Successfully")
        else:
            messages.error(request, "Login Failed")

    return render(request, "home.html")


def ulogin(request):
    pass


def ulogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logout")
        return render(request, "auth/logout.html")
    return redirect("home")
