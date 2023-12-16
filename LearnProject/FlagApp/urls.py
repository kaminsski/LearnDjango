from django.urls import path
from .views import *

urlpatterns = [
   
    path("flag", flag, name="flag"),
    path("records", records, name="records"),





]