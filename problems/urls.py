from django.urls import path

from . import views

app_name = "problems"

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("contact/<int:id>", views.update_problem, name="update")
]