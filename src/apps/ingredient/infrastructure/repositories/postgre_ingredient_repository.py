from ...domain import Ingredient, IngredientRepository
from ..models import Ingredient as IngredientModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreIngredientRepository(IngredientRepository):
    
    def __init__(self, ingredient_model):
        self.ingredient_model = ingredient_model
        self.session = Session()

    def find_all_ingredients(self):
        ingredients = self.session.query(self.ingredient_model).all()
        
        return ingredients

    def find_ingredient_by_id(self, id: str):
        ingredient = self.session.query(self.ingredient_model).filter_by(aggregate_id=id).first()

        return ingredient

    def save_ingredient(self, ingredient: Ingredient):
        ingredient = IngredientModel(
            name=ingredient._name,
            availability=ingredient.availability,
            unit=ingredient.unit,
            aggregate_id=ingredient._id
        )

        try: 
            self.session.add(ingredient)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def delete_ingredient(self, ingredient: Ingredient):
        try:
            self.session.delete(ingredient)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())

    def update_ingredient(self, ingredient: Ingredient):
        pass