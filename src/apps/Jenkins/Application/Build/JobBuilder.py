from src.apps.Jenkins.Domain.ServerRepository import ServerRepository
from src.apps.Jenkins.Domain.JobParams import JobParams
from typing import Type


class JobBuilder:
    def __init__(self, repository: Type[ServerRepository]) -> None:
        self.repository = repository

    def exec(self, name: str, params: JobParams) -> None:
        self.repository.build(name, params)
