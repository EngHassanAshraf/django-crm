from django.urls import path
from .views import home, ulogin, ulogout


urlpatterns = [
    path("", home, name="home"),
    path("login/", ulogin, name="login"),
    path("logout/", ulogout, name="logout"),
]
