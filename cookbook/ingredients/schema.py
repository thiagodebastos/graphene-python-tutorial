from graphene import List
from graphene_django.types import DjangoObjectType
from cookbook.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(object):
    all_categories= List(CategoryType)
    all_ingredients = List(IngredientType)


    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimise query count in the resolve method
        return Ingredient.objects.select_related('category').all()
