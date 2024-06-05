from core.domain.entity.domain_entity import DomainEntity

class Menu(DomainEntity[str]):
    def __init__(self, _id: str, name: str) -> None:
        super().__init__(_id)
        self.name = name
 
