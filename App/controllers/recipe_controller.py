from App.models import Recipe
from App.database import db


def getRecipes():
    recipes=Recipe.query.all()
    if not recipes:
        return []
    recipes_list = [recipe.get_json() for recipe in recipes]
    return recipes_list

def createRecipe(userid,title,ingredients, instructions):
    recipe=Recipe(id=userid,title=title,ingredients=ingredients,instructions=instructions)
    if recipe:
        return recipe
    return None