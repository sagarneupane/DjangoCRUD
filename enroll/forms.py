from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Enter Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                label="Re-Enter your Password")

    # password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        widgets = {"username": forms.TextInput(attrs={"class": 'form-control'}),
                   "email": forms.EmailInput(attrs={"class": 'form-control'}),
                   }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class ChangePassForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                    label="Enter New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                    label="Confirm New Password")


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        widgets = {"email": forms.EmailInput(attrs={"class": "form-control"}),
                   "first_name": forms.TextInput(attrs={"class": "form-control"}),
                   "last_name": forms.TextInput(attrs={"class": "form-control"}),
                   }


class AdminEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "is_superuser", "is_staff","is_active"]
        widgets = {"email": forms.EmailInput(attrs={"class": "form-control"}),
                   "first_name": forms.TextInput(attrs={"class": "form-control"}),
                   "last_name": forms.TextInput(attrs={"class": "form-control"}),
                   "is_staff": forms.CheckboxInput(attrs={"class": "form-check-input"}),
                   "is_superuser": forms.CheckboxInput(attrs={"class": "form-check-input"}),
                   "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
                   }
