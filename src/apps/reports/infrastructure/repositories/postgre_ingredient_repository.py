from ...application.repositories.ingredient_repository import IngredientRepository
from core.infrastructure.db_session.postgre_session import Session

class PostgreIngredientRepository(IngredientRepository):
    
    def __init__(self):
        self.session = Session()
    
    def get_ingredients_available_quantities(self):
        try:
            result = self.session.execute('SELECT name, quantity FROM "Ingredient"')
            ingredients = [{"name": row.name, "quantity": row.quantity} for row in result]
            return ingredients
        except Exception as e:
            raise Exception(e.__str__())