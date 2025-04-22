from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    bob=create_user('bob', 'bobpass')
    recipe=bob.createRecipe(userid,title,ingredients, instructions)
  
