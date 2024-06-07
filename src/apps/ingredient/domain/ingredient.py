from core.domain.entity.domain_entity import DomainEntity

class Ingredient(DomainEntity[str]):
    def __init__(self, _id: str, name: str, availability: int, unit: str) -> None:
        super().__init__(_id)
        self._name = name
        self.availability = availability
        self.unit = unit
