from django.urls import path
from .views import home, register, ulogout

urlpatterns = [
    path("", home, name="home"),
    path("register/", home, name="register"),
    path("logout/", ulogout, name="logout"),
]
