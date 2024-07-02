from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..repositories.postgre_ingredient_repository import PostgreIngredientRepository
from ..repositories.postgre_order_repository import PostgreOrderRepository
from ...application.queries.get_ingredients_available_quantities_query.get_ingredients_available_quantities_query import GetIngredientAvailableQuantitiesService
from ...application.queries.get_orders_by_client_query.get_orders_by_client_query import GetOrdersByClientsService
from starlette.responses import HTMLResponse

router = APIRouter(tags=['Reports'])
templates = Jinja2Templates(directory="templates/")
ingredientRepository = PostgreIngredientRepository()
orderRepository = PostgreOrderRepository


@router.get("/report/inventory", response_class=HTMLResponse)
async def get_ingredients_available_quantities(request: Request):
    report = GetIngredientAvailableQuantitiesService(ingredientRepository)
    response = report.execute()
    templates.TemplateResponse("index.html", {"request": request, "available_quantity_ingredient": report['available_quantity_ingredient']})
    
    return response.unwrap()

@router.get("report/orders_client", response_class=HTMLResponse)
async def get_orders_by_client(request: Request):
    report = GetOrdersByClientsService(orderRepository)
    response = report.execute()
    templates.TemplateResponse("index.html", {"request": request, "orders_by_client": report['orders_by_client']})
    
    return response.unwrap()

# @app.get("/report/sales", response_class=HTMLResponse)
# async def sales_report(request: Request):
#     report = report_service.generate_report()
#     return templates.TemplateResponse("sales_report.html", {"request": request, "total_sales": report['total_sales']})

# @app.get("/report/ingredients", response_class=HTMLResponse)
# async def ingredients_report(request: Request):
#     report = report_service.generate_report()
#     return templates.TemplateResponse("ingredients_report.html", {"request": request, "most_used_ingredients": report['most_used_ingredients']})

# @app.get("/report/inventory", response_class=HTMLResponse)
# async def inventory_report(request: Request):
#     report = report_service.generate_report()
#     return templates.TemplateResponse("inventory_report.html", {"request": request, "inventory_status": report['inventory_status']})

@router.get('/report_inventory')
def index(request: Request):
    return templates.TemplateResponse('inventory/index.html', {"request": request})

@router.get('/report_orders')
def index(request: Request):
    return templates.TemplateResponse('orders/index.html', {"request": request})