from django import forms


class user_email_Form(forms.Form):
    user_email = forms.EmailField(widget=forms.TextInput(attrs={"id" : 'email'}))


class user_password_Form(forms.Form):
    user_password = forms.IntegerField(widget=forms.NumberInput(attrs={"id" : 'password'}))