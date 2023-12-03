from django.http import HttpResponse
from django.shortcuts import render


def list(request) -> HttpResponse:
    return render(
        request=request,
        template_name="recipes/recipes.html",
        context={}
    )
