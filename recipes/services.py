from dataclasses import dataclass

from .models import Recipe


@dataclass
class RecipeDTO:
    title: str
    description: str
    category: str

    @classmethod
    def from_django_model(cls, recipe: Recipe) -> 'RecipeDTO':
        return cls(
            title=Recipe.title,
            description=Recipe.description,
            category=Recipe.category
        )


class NormalRecipeService:
    @staticmethod
    def list() -> list[RecipeDTO]:
        return [RecipeDTO.from_django_model(r) for r in Recipe.objects.all()]
