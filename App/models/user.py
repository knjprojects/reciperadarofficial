from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models import Recipe, Review
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def createRecipe(userid,title,ingredients, instructions):
        recipe=Recipe(id=userid,title=title,ingredients=ingredients,instructions=instructions)
        if recipe:
            return recipe
        return None
    def reviewRecipe(self,recipeid,comment,rating):
        rev=Review(userid=self.id,recipeid=recipeid,comment=comment,rating=rating)
        if rev:
            return rev
        return None