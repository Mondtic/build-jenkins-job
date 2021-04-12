from src.apps.Jenkins.Domain.ServerRepository import ServerRepository

class BuildFinder:
    def __init__(self, repository: Type[ServerRepository]) -> None:
        self.repository = repository
    
    def exec(self, name:str, number:int) -> str:
        return self.repository.get_status(name, number)

    def number(self) -> int:
        return self.repository.get_number()