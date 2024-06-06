from ....domain import Dish, DishRepository
from .types import CreateDishDto
from core.application.services.application_service import Service
from core.application.results.result import Result
from core.infrastructure.providers.uuid_service import UUIDService

class CreateDishService(Service[CreateDishDto, str]):

    def __init__(self, dish_repository: DishRepository) -> None:
        super().__init__()
        self.dish_repository = dish_repository
        self.idGenerator = UUIDService

    def execute(self, data: CreateDishDto) -> Result[str]:
        _id = self.idGenerator.generate_id()
        #TODO:
        #data.ingredients -> Esta es la lista de ids de los ingredientes 
        #Agregar logica de validacion de existencia de ingredientes
        #Si no se tienen todos los ingredientes, no se crea el plato
        dish = Dish(_id, data.name, data.description, data.price, data.disponibility)
        self.dish_repository.save_dish(dish)

        return Result[str].make_success(value=_id)