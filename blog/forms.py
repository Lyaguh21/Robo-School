from django import forms
from .models import registration_form


class user_registration_Form(forms.ModelForm):
    class Meta:
        model = registration_form
        fields = "__all__"