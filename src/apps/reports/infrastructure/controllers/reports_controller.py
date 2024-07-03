from fastapi import APIRouter, Request
from typing import List
from fastapi.templating import Jinja2Templates
from ..repositories.postgre_ingredient_repository import PostgreIngredientRepository
from ..repositories.postgre_order_repository import PostgreOrderRepository
from ...application.queries.get_all_ingredients_with_quantities_query.get_all_ingredients_with_quantities_query import GetAllIngredientWithQuantitiesService
from ...application.queries.get_orders_by_menu_query.get_orders_by_menu_query import GetOrdersByMenuService
from starlette.responses import HTMLResponse
from ....ingredient.infrastructure.models.postgre_ingredient_model import Ingredient
from ....order.infrastructure.models.postgre_order_model import OrderModel
from ....menu.infrastructure.models.postgre_menu_model import MenuModel
from ....dish.infrastructure.models.postgre_dish_model import DishModel
from ....user.infrastructure.models.postgre_user_model import UserModel
from ...application.queries.get_total_sales_from_orders_by_dish_query.get_total_sales_from_orders_by_dish_query import GetTtotalSalesFromOrdersByDishService
from ....auth.infrastructure.middlewares.verify_token_route import VerifyTokenRoute
from ...application.queries.get_frequent_clients_query.get_frequent_clients_query import GetFrequentClientsService
from ...application.queries.get_frequent_dishes_query.get_frequent_dishes_query import GetFrequentDishesService

router = APIRouter(route_class=VerifyTokenRoute, tags=['Reports'])
templates = Jinja2Templates(directory="templates/")
ingredient_model = Ingredient
ingredientRepository = PostgreIngredientRepository(ingredient_model)
order_model = OrderModel
menu_model = MenuModel
dish_model = DishModel
client_model = UserModel
orderRepository = PostgreOrderRepository(order_model, menu_model, dish_model, client_model)

@router.get("/report/inventory", response_class=HTMLResponse)
async def get_all_ingredients_with_quantities(request: Request):
    report = GetAllIngredientWithQuantitiesService(ingredientRepository)
    response = report.execute()
    data = response.value
    return templates.TemplateResponse("inventory/inventory.html", {"request": request, "available_quantity_ingredient": data})

@router.get("/report/orders", response_class=HTMLResponse)
async def get_orders_by_menu(request: Request):
    report = GetOrdersByMenuService(orderRepository)
    response = report.execute()
    data = response.value
    return templates.TemplateResponse("orders/orders.html", {"request": request, "orders": data})

@router.get("/report/orders/total_sales", response_class=HTMLResponse)
async def get_total_sales_from_orders_by_dish(request: Request):
    report = GetTtotalSalesFromOrdersByDishService(orderRepository)
    response = report.execute()
    data = response.value
    return templates.TemplateResponse("orders/total_sales.html", {"request": request, "total_sales": data})

@router.get("/report/clients", response_class=HTMLResponse)
async def get_frequent_clients(request: Request):
    report = GetFrequentClientsService(orderRepository)
    response = report.execute()
    data = response.value
    return templates.TemplateResponse("orders/clients.html", {"request": request, "frequent_clients": data})

@router.get("/report/dishes", response_class=HTMLResponse)
async def get_frequent_dishes(request: Request):
    report = GetFrequentDishesService(orderRepository)
    response = report.execute()
    data = response.value
    return templates.TemplateResponse("orders/dishes.html", {"request": request, "frequent_dishes": data})