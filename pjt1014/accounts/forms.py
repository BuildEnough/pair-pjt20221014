from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PJTuser

from django.contrib.auth import get_user_model


class NewB(UserCreationForm):
    class Meta:
        model = PJTuser
        fields = ["username"]


class OldB(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
