from fastapi import FastAPI
from apps.ingredient.infrastructure.controllers.ingredient_controller import router as ingredient_router
from apps.menu.infrastructure.controllers.menu_controller import router as menu_router


app = FastAPI()

app.include_router(ingredient_router)
app.include_router(menu_router)
