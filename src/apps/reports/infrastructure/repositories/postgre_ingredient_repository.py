from ...application.repositories.ingredient_repository import IngredientRepository
from core.infrastructure.db_session.postgre_session import Session

class PostgreIngredientRepository(IngredientRepository):
    
    def __init__(self):
        self.session = Session()
    
    def get_ingredients_available_quantities(self):
        try:
            # Ejecuta una consulta SQL para obtener las cantidades disponibles de todos los ingredientes
            result = self.session.execute("SELECT ingredient_name, amount FROM ingredients")
            # Convierte el resultado en una lista de diccionarios
            ingredients = [{"name": row.ingredient_name, "amount": row.amount} for row in result]
            return ingredients
        except Exception as e:
            raise Exception(str(e))