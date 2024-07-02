from ....domain import Dish, DishRepository
from ...exceptions.no_ingredients_in_stock import NoIngredientInStockException
from .types import CreateDishDto
from .....ingredient.application.queries.get_ingredient_by_id_query.get_ingredient_by_id import GetIngredientByIdService
from .....ingredient.application.exceptions.incomplete_ingredient_list import IncompleteIngredientListException 
from .....ingredient.application.queries.get_ingredients_list_query.get_ingredients_list import GetIngredientsListService 
from core.application.services.application_service import Service
from .....ingredient.application.queries.get_ingredient_by_id_query.get_ingredient_by_id import GetIngredientByIdService
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateDishService(Service[CreateDishDto, str]):

    def __init__(self, dish_repository: DishRepository, get_ingredients_list: GetIngredientsListService) -> None:
        super().__init__()
        self.dish_repository = dish_repository
        self.idGenerator = UUIDService
        self.get_ingredients_list = get_ingredients_list

    def execute(self, data: CreateDishDto) -> Result[str]:
        _id = self.idGenerator.generate_id()
        #TODO:
        #data.ingredients -> Esta es la lista de ids de los ingredientes 
        #Agregar logica de validacion de existencia de ingredientes
        #Si no se tienen todos los ingredientes, no se crea el plato
        dish = Dish(_id, data.name, data.description, data.price, data.disponibility)
        self.dish_repository.save_dish(dish)

        return Result[str].make_success(value=_id)