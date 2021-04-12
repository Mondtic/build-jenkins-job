import jenkins
import json
import requests
import time
from typing import Any
from src.apps.Jenkins.Domain.ServerRepository import ServerRepository

class ServerJenkinsRepository(ServerRepository):
    def __init__(self, url: str, token: str, username: str):
        self.__url = url
        self.__token = token
        self.__username = username

        #Start Connection
        self.__connection = jenkins.Jenkins(self.__url, username=self.__username, password=self.__token)

    def build(self, name:str, params:str) -> None:
        self.__connection.build_job(name, parameters=json.loads(params), token=self.__token)
    
    def __get_queue_info(self) -> None:
        self.__queue_info = self.__connection.get_queue_info()
    
    def __get_queue_id(self) -> int:
        self.__get_queue_info()
        return self.__queue_info[0].get('id')

    def __get_job_info(self):
        protocol,domain = url.split("://")
        url = f"{protocol}://{self.__username}:{self.__token}@{domain}/queue/item/{self.__get_queue_id()}/api/json?pretty=true"
        info = requests.get(url).json()
        return info

    def get_number(self) -> int:
        while "executable" not in (info := self.__get_job_info()):
            time.sleep(3)
        return info["executable"]["number"]
    
    def get_status(self, name, number) -> str:
        build_info = self.__connection.get_build_info(name=name, number=number)
        return build_info["result"]