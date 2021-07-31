import jenkins
import json
import requests
import time
from src.apps.Jenkins.Domain.ServerRepository import ServerRepository
from src.apps.Jenkins.Domain.JobParams import JobParams


class ServerJenkinsRepository(ServerRepository):
    def __init__(self, url: str, token: str, username: str, ssl_verify=False):
        self.__url = url
        self.__token = token
        self.__username = username
        self.__ssl_verify = ssl_verify

        # Start Connection
        self.__connection = jenkins.Jenkins(self.__url, username=self.__username, password=self.__token)
        self.__connection._session.verify = ssl_verify
        
    def build(self, name: str, params: JobParams) -> None:
        self.__name = name
        queue_id = self.__connection.build_job(name, parameters=json.loads(params), token=self.__token)
        self.__queue_id = queue_id

    def __get_queue_info(self):
        protocol, domain = self.__url.split("://")
        url = f"{protocol}://{self.__username}:{self.__token}@{domain}/queue/item/{self.__queue_id}/api/json?pretty=true"
        info = requests.get(url, verify=self.__ssl_verify).json()
        return info

    def get_number(self) -> int:
        while "executable" not in (info := self.__get_queue_info()):
            time.sleep(3)
        return info["executable"]["number"]

    def get_status(self, number) -> str:
        build_info = self.__connection.get_build_info(name=self.__name, number=number)
        return build_info["result"]
