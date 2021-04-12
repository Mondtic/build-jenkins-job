from src.apps.Jenkins.Domain.ServerRepository import ServerRepository
from typing import Type


class BuildFinder:
    def __init__(self, repository: Type[ServerRepository]) -> None:
        self.repository = repository

    def exec(self, number: int) -> str:
        return self.repository.get_status(number)

    def number(self) -> int:
        return self.repository.get_number()
