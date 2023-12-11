from django.http import HttpResponse
from django.shortcuts import render

from .services import NormalRecipeService as service


def list(request) -> HttpResponse:
    """
    # filtrowanie
    c = Category.objects.get(name="vege")
    Recipe.objects.filter(category=c)

    c.recipes.all() # pod warunkiem, że mamy ustawione related_name
    """

    results = service.list()
    return render(
        request=request,
        template_name="recipes/recipes.html",
        context={"recipes": results}
    )
