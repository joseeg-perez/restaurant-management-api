from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..repositories.postgre_ingredient_repository import PostgreIngredientRepository
from ...application.queries.get_ingredients_available_quantities_query.get_ingredients_available_quantities_query import GetIngredientAvailableQuantitiesService
from starlette.responses import HTMLResponse

router = APIRouter(tags=['Reports'])
templates = Jinja2Templates(directory="templates/")
ingredientRepository = PostgreIngredientRepository()

@router.get("/report/inventory", response_class=HTMLResponse)
async def get_ingredients_available_quantities(request: Request):
    report = GetIngredientAvailableQuantitiesService(ingredientRepository)
    response = report.execute()
    templates.TemplateResponse("index.html", {"request": request, "available_quantity_ingredient": report['available_quantity_ingredient']})
    
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

@router.get('/inventory')
def index(request: Request):
    return templates.TemplateResponse('ingredients/index.html', {"request": request})