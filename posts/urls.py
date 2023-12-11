from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "posts"

urlpatterns = [
    path("posts/", views.display_post, name="display_post"),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path("posts/add", views.add_post, name="add_post"),
    path("posts/<int:id>", views.post_details, name="details"),
]
