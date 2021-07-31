from src.apps.Jenkins.Domain.ServerRepository import ServerRepository
from typing import Type


class BuildFinder:
    def __init__(self, repository: Type[ServerRepository], name: str) -> None:
        self.repository = repository
        self.name = name
        self.consoleLines = 0

    def exec(self, number: int) -> str:

        consoleLines = self.repository.get_build_console_output(self.name, number).split("\n")
        consoleLinesCount = len(consoleLines)
        for i in range(self.consoleLines, consoleLinesCount):
            print(consoleLines[i])

        self.consoleLines = consoleLinesCount

        return self.repository.get_status(number)
    
    def number(self) -> int:
        return self.repository.get_number()    
