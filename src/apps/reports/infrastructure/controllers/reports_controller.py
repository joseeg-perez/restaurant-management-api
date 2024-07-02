from fastapi import APIRouter, Request, Query
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
from ...application.queries.get_total_sales_from_orders_by_dish_query.get_total_sales_from_orders_by_dish_query import GetTtotalSalesFromOrdersByDishService


router = APIRouter(tags=['Reports'])
templates = Jinja2Templates(directory="templates/")
ingredient_model = Ingredient
ingredientRepository = PostgreIngredientRepository(ingredient_model)
order_model = OrderModel
menu_model = MenuModel
dish_model = DishModel
orderRepository = PostgreOrderRepository(order_model, menu_model, dish_model)


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