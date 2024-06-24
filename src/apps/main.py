from fastapi import FastAPI
from apps.ingredient.infrastructure.controllers.ingredient_controller import router as ingredient_router
from apps.menu.infrastructure.controllers.menu_controller import router as menu_router
from apps.dish.infrastructure.controllers.dish_controller import router as dish_router
from apps.user.infrastructure.controllers.user_controller import router as user_router
from apps.reports.infrastructure.controllers.reports_controller import router as report_router

app = FastAPI()

app.include_router(ingredient_router)
app.include_router(menu_router)
app.include_router(dish_router)
app.include_router(user_router)
app.include_router(report_router)
