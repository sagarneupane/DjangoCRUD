from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("login/", views.signin, name="signin"),
    path("logout/", views.signout, name="signout"),
    path("profile/", views.profile, name="profile"),
    path("changepass/", views.changepass, name="changepass"),
    path("fullprofile/<int:id>", views.view_profile, name="view_profile"),
    path("editprofile/", views.edit_profile, name="edit_profile"),
    path("viewusers/", views.view_other_user, name="viewusers"),
    path("editusers/<int:id>", views.edit_other_user, name="editusers"),
    path("deleteusers/<int:id>", views.delete_user, name="deleteusers"),
]
