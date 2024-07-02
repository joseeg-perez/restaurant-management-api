from ....domain import Dish, DishRepository
from .types import CreateDishDto
from .....ingredient.application.queries.get_ingredient_by_id_query.get_ingredient_by_id import GetIngredientByIdService
from .....ingredient.application.exceptions.incomplete_ingredient_list import IncompleteIngredientListException 
from .....ingredient.application.queries.get_ingredients_list_query.get_ingredients_list import GetIngredientsListService 
from core.application.services.application_service import Service
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

        ingredients_list = self.get_ingredients_list.execute(data.ingredients)
        if( ingredients_list.is_failure() ):
            return Result[str].make_failure(error=IncompleteIngredientListException())

        dish = Dish(_id, data.name, data.description, data.price, data.availability)
        self.dish_repository.save_dish(dish, data.menu_id)

        return Result[str].make_success(value=_id)