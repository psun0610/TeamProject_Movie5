from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
    path("password/", views.change_password, name="change_password"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
