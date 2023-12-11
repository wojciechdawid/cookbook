from django.http import HttpResponse
from django.shortcuts import render

from .services import NormalRecipeService as service


def list(request) -> HttpResponse:
    results = service.list()
    return render(
        request=request,
        template_name="recipes/recipes.html",
        context={"recipes": results}
    )
