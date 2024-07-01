from typing import List
from sqlalchemy import update
from ...domain import Ingredient, IngredientRepository
from ..models import Ingredient as IngredientModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreIngredientRepository(IngredientRepository):
    
    def __init__(self, ingredient_model: IngredientModel):
        self.ingredient_model = ingredient_model
        self.session = Session()

    def find_all_ingredients(self):
        ingredients = self.session.query(self.ingredient_model).all()
        
        return ingredients

    def find_ingredient_by_id(self, id: str):
        ingredient = self.session.query(self.ingredient_model).filter_by(entity_id=id).first()

        return ingredient
    
    def get_ingredient_list(self, ingredients_ids: List[str]) -> List[Ingredient]:
        try:
            ingredients = self.session.query(self.ingredient_model).filter(IngredientModel.entity_id.in_(ingredients_ids)).all()
            return ingredients

        except Exception as e:
            raise Exception(e.__str__())

    def save_ingredient(self, ingredient: Ingredient):
        ingredient = IngredientModel(
            entity_id=ingredient._id,
            name=ingredient._name,
            quantity=ingredient._quantity,
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

    def update_ingredient(self, ingredients: List[Ingredient]):
        try: 
            for ingredient in ingredients:
                stmt = (
                    update(IngredientModel).
                    where(IngredientModel.entity_id == ingredient.entity_id).
                    values(
                        name=ingredient.name,
                        quantity=ingredient.quantity,
                    )
                )
                self.session.execute(stmt)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())
        
        