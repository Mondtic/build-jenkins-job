import json
from src.apps.Jenkins.Domain.JobParamsIsNotValidJson import JobParamsIsNotValidJson


class JobParams(str):
    def __init__(self, value='', encoding=None, errors='strict') -> None:
        self.__is_a_json()

    def __is_a_json(self) -> None:
        try:
            json.loads(self)
        except ValueError:
            raise JobParamsIsNotValidJson
