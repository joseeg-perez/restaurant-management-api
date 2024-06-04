from fastapi import APIRouter
from ...application.queries.get_all_products import GetAllProductsFromInventory
from ..repositories.postgre_product_repository import PostgreProductRepository
from ..models.product_postgre_model import Product
from .dtos.create_product_dto import CreateProductDto

router = APIRouter()
product_model = Product
repository = PostgreProductRepository(product_model)

@router.get("/products")
def  get_products():
    service = GetAllProductsFromInventory(repository)
    response = service.execute()
    return response.unwrap()

@router.post('/products')
def create_product(product: CreateProductDto):
    print(product)

    return