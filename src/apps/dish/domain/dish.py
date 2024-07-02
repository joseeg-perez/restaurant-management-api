from core.domain.entity.domain_entity import DomainEntity

class Dish(DomainEntity[str]):
    def __init__(self, _id: str, name: str, description: str, price: float, availability: bool) -> None:
        super().__init__(_id)
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability