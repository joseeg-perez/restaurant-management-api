from core.domain.entity.domain_entity import DomainEntity

class Ingredient(DomainEntity[str]):
    def __init__(self, _id: str, name: str, quantity: int) -> None:
        super().__init__(_id)
        self._name = name
        self._quantity = quantity