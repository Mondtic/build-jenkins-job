import jenkins
import json
import requests
import time
from typing import Any
from src.apps.Jenkins.Domain.ServerRepository import ServerRepository
from src.apps.Jenkins.Domain.JobParams import JobParams

class ServerInMemoryRepository(ServerRepository):
    def __init__(self, queue_number:int, build_number:int, status:str):
        self.__queue_number = queue_number
        self.__build_number = build_number
        self.__status = status

    def build(self, name:str, params: JobParams) -> None:
        self.queue_id = self.__queue_number

    def get_number(self) -> int:
        return self.__build_number
    
    def get_status(self, number) -> str:
        return self.__status