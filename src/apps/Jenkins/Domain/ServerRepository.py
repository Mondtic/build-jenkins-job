import abc
from typing import Type, Optional
from src.apps.Jenkins.Domain.JobParams import JobParams

class ServerRepository:

    @abc.abstractmethod
    def build(self, name:str, params:JobParams) -> None: pass

    @abc.abstractmethod
    def get_number(self) -> int: pass

    @abc.abstractmethod
    def get_status(self, number: int) -> str: pass