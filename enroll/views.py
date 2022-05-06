from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, ChangePassForm, UserEditForm, AdminEditForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


# Create your views here.
# Register User
def signup(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, level=50, message="User Registration SuccessFull", extra_tags="primary")
            return redirect("signup")
        else:
            messages.add_message(request, level=50, message="Fix out the errors", extra_tags="danger")
    else:
        fm = UserForm()
    context = {"form": fm}
    return render(request, "signup.html", context)


# login User
def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                user = authenticate(username=fm.cleaned_data['username'], password=fm.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully Logged In")
                    return redirect("profile")
        else:
            fm = LoginForm()
        context = {"form": fm}
        return render(request, "signin.html", context)
    else:
        return redirect("profile")


# Logout User
def signout(request):
    logout(request)
    return redirect("signin")


# View Profile
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("signin")


# View More about Profile
def view_profile(request, id):
    if request.user.is_authenticated:
        user = User.objects.all().filter(id=id)
        context = {"users": user}
        return render(request, 'fullprofile.html', context)
    else:
        return redirect("signin")


# Edit Profile
def edit_profile(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.method == "POST":
                fm = UserEditForm(instance=request.user, data=request.POST)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "User Profile Updated Successfully")
                    return redirect("profile")
            else:
                fm = UserEditForm(instance=request.user)
        else:
            if request.method == "POST":
                fm = AdminEditForm(instance=request.user, data=request.POST)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "User Profile Updated Successfully")
                    return redirect("profile")
            else:
                fm = AdminEditForm(instance=request.user)
        context = {"form": fm}
        return render(request, "editprofile.html", context)
    else:
        return redirect("signin")


# Change Password
def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = ChangePassForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password Successfully Changed")
                update_session_auth_hash(request, request.user)
                return redirect("profile")
        else:
            fm = ChangePassForm(user=request.user)
        context = {"form": fm}
        return render(request, 'changepassword.html', context)
    else:
        return redirect("signin")


def view_other_user(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {"users": users}
        return render(request, 'viewotheruser.html', context)
    else:
        return redirect("profile")


def edit_other_user(request, id):
    if request.user.is_superuser:
        users = User.objects.get(pk=id)
        if request.method == "POST":
            fm = AdminEditForm(instance=users, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "User successfully Updated")
                return redirect("viewusers")
        else:
            fm = AdminEditForm(instance=users)
        context = {"form": fm}
        return render(request, 'editother.html', context)
    else:
        return redirect("profile.html")


def delete_user(request, id):
    users = User.objects.get(pk=id)
    users.is_active = False
    users.save()
    messages.success(request, "User can't be able to log in again")
    return redirect("viewusers")
