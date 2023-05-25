from django.urls import path
from .views import home
app_name = "vpn_generator"

urlpatterns = [
    path("" , home , name="home")
]
