from django.urls import path

from . import views

app_name = "problems"

urlpatterns = [
    path("posts/contact/", views.contact, name="contact"),
]