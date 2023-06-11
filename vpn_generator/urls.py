from django.urls import path
from .views import home , successful , unsuccessful
app_name = "vpn_generator"

urlpatterns = [
    path("" , home , name="home"),
    path("successful/", successful , name="successful"),
    path("unsuccessful/", unsuccessful, name="unsuccessful")

]
