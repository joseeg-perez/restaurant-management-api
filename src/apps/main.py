from fastapi import FastAPI
from apps.product.infrastructure.controllers.product_controller import router as inventory_router


app = FastAPI()

app.include_router(inventory_router)