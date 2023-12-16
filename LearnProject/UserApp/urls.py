from django.urls import path
from UserApp.views import *

urlpatterns = [
    path("", index, name="home"),
    
    path("profile", profile, name="profile"),
    path("settings", settings, name="settings"),
    path("login", login, name="login"),
    path("logout", log_out, name="log_out"),




]
