import abc
from typing import Type, Optional

class ServerRepository:

    @abc.abstractmethod
    def build(self, name:str, params:str) -> None: pass

    @abc.abstractmethod
    def get_number(self) -> int: pass

    @abc.abstractmethod
    def get_status(self, number: int) -> str: pass