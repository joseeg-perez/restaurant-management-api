from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class DomainEntity(ABC, Generic[T]):

    def __init__(self, id: T) -> None:
        self._id = id