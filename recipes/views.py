from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe


def list(request) -> HttpResponse:
    results = Recipe.objects.all()
    return render(
        request=request,
        template_name="recipes/recipes.html",
        context={"recipes": results}
    )
