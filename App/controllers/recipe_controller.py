from App.models import Recipe
from App.database import db


def getRecipes():
    recipes=Recipe.query.all()
    if not recipes:
        return []
    recipes_list = [recipe.get_json() for recipe in recipes]
    return recipes_list