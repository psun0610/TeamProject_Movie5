from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Myform(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
        ]
