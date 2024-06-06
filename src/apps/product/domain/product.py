from core.domain.entity.domain_entity import DomainEntity

class Product(DomainEntity[str]):
    def __init__(self, _id: str, name: str, price: float, stock: int) -> None:
        super().__init__(_id)
        self._name = name
        self._price = price
        self.stock = stock
