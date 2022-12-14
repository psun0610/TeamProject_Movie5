from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("<int:review_pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
