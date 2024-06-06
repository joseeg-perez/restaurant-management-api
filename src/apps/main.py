from fastapi import FastAPI
from apps.product.infrastructure.controllers.product_controller import router as inventory_router
from apps.menu.infrastructure.controllers.menu_controller import router as menu_router
from apps.dish.infrastructure.controllers.dish_controller import router as dish_router


app = FastAPI()

app.include_router(inventory_router)
app.include_router(menu_router)
app.include_router(dish_router)
