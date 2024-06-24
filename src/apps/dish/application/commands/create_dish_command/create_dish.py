from ....domain import Dish, DishRepository
from ...exceptions.no_ingredients_in_stock import NoIngredientInStockException
from .types import CreateDishDto
from core.application.services.application_service import Service
from .....ingredient.application.queries.get_ingredient_by_id_query.get_ingredient_by_id import GetIngredientByIdService
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateDishService(Service[CreateDishDto, str]):

    def __init__(self, dish_repository: DishRepository) -> None:
        super().__init__()
        self.dish_repository = dish_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateDishDto) -> Result[str]:
        _id = self.idGenerator.generate_id()
        all_ingredients = GetIngredientByIdService()
        
        for ingredient in data.ingredients:
            ingredients = all_ingredients.execute(ingredient)
            
            if  ingredients.is_failure():
                return Result[str].make_failure(error=NoIngredientInStockException())
        #TODO:
        #Hacer un update por cada uno de los ingredientes que existan en el plato
        #donde se le reste uno a la cantidad para quitarlo del inventario
        #rellenar con esos datos la tabla de Ingrediente-plato 
        
        # ingredient.quantity -=1
        # if ingredient.quantity < 0:
        #     return Result[str].make_failure(error=NoIngredientInStockException())
    
        # self.Ingredient_dish_repository.update_ingredient(ingredient)
        # self.Ingredient_dish_repository.add_ingredient_to_dish(ingredient, _id)
        
        dish = Dish(_id, data.name, data.description, data.price, data.disponibility)
        self.dish_repository.save_dish(dish)

        return Result[str].make_success(value=_id)