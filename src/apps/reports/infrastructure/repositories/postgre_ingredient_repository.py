from ...application.repositories.ingredient_repository import IngredientRepository
from ....ingredient.infrastructure.models.postgre_ingredient_model import Ingredient as IngredientModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreIngredientRepository(IngredientRepository):
    
    def __init__(self, ingredient_model: IngredientModel):
        self.ingredient_model = ingredient_model
        self.session = Session()
    
    def get_all_ingredients_with_quantities(self):
        try:
            result = self.session.query(self.ingredient_model.name, self.ingredient_model.quantity).all()
            ingredients = [{"name": row.name, "quantity": row.quantity} for row in result]
            return ingredients
        
        except Exception as e:
            raise Exception(e.__str__())