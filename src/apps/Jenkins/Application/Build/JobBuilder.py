from src.apps.Jenkins.Domain.ServerRepository import ServerRepository

class JobBuilder:
    def __init__(self, repository: Type[ServerRepository]) -> None:
        self.repository = repository
    
    def exec(self, name:str, params:str) -> None:
        self.repository.build(name, params)