import graphene
from graphene import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from cookbook.ingredients.models import Category, Ingredient, Recipe


class RecipeType(DjangoObjectType):
    """
    A collection of ingredients that makes up a meal recipe.
    """
    class Meta:
        model = Recipe
        interfaces = (Node, )
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "ingredients": ["exact"]
        }


class CategoryType(DjangoObjectType):
    """
    Used to categorise ingredients.
    """
    class Meta:
        model = Category
        interfaces = (Node, )
        filter_fields = ["name", "ingredients"]


class IngredientType(DjangoObjectType):
    """
    An ingredient that makes up part of a recipe.
    """
    class Meta:
        model = Ingredient
        interfaces = (Node, )
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "category": ["exact"],
            "category__name": ["exact"],
        }


class Query(object):
    """
    Get a category by ID or name.
    """
    category = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String()
    )

    ingredient = graphene.Field(
        IngredientType, id=graphene.Int(), name=graphene.String()
    )

    recipe = graphene.Field(
        RecipeType, id=graphene.Int(), name=graphene.String()
    )

    all_categories = graphene.List(CategoryType)

    all_ingredients = graphene.List(IngredientType)

    all_recipes = graphene.List(RecipeType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimise query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Recipe.objects.get(pk=id)

        if name is not None:
            return Recipe.objects.get(name=name)

        return None
