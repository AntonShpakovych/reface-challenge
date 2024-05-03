from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views


urlpatterns = [
    path("auth/", views.LoginOrSignUp.as_view(), name="auth-all"),
    path("logout/", LogoutView.as_view(), name="auth-logout"),
]


app_name = "user"
