import pytest
from src.apps.Jenkins.Domain.JobParams import JobParams
from src.apps.Jenkins.Domain.JobParamsIsNotValidJson import JobParamsIsNotValidJson

class TestJobBuilder:
    def test_should_return_a_exception_if_jobparams_is_not_a_valid_json(self):
        with pytest.raises(JobParamsIsNotValidJson):
            params = JobParams("FAIL")
    
    def test_should_set_a_jobparams_type(self):
        params = JobParams('{"key": "value"}')
        assert type(params) == JobParams