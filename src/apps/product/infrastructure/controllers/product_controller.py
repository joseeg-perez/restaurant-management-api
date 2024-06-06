from fastapi import APIRouter, status, HTTPException    
from ...application.commands import CreateProductService, DeleteProductService
from ...application.queries import GetProductByIdService, GetAllProductsService
from .dtos import CreateProductDto, GetProductByIdDto, DeleteProductDto
from ..repositories import PostgreProductRepository
from ..models import Product

router = APIRouter(tags=['Products'])
product_model = Product
repository = PostgreProductRepository(product_model)

@router.get("/products")
def get_all_products():
    service = GetAllProductsService(repository)
    response = service.execute()
    
    return response.unwrap()

@router.get('/product/{id}')
def get_product_by_id(id: str):
    service = GetProductByIdService(repository)
    response = service.execute(GetProductByIdDto(product_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)

    return response.unwrap()

@router.post('/products')
def create_product(product: CreateProductDto):
    service = CreateProductService(repository)
    response = service.execute(product)

    return response.unwrap()

@router.delete('/product/{id}')
def delete_product(id: str):
    service = DeleteProductService(repository)
    response = service.execute(DeleteProductDto(product_id=id))
    if response.is_failure():    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.error.message)
    
    return response.unwrap()