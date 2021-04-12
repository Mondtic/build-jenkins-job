from src.apps.Jenkins.Application.Build.JobBuilder import JobBuilder
from src.apps.Jenkins.Infrastructure.ServerInMemoryRepository import ServerInMemoryRepository


class TestJobBuilder:
    def test_should_build_a_job(self):
        repository = ServerInMemoryRepository(
            queue_number=22,
            build_number=1,
            status="SUCCESS"
        )
        builder = JobBuilder(repository=repository)
        builder.exec(name="test_job", params="{}")

        assert repository.queue_id == 22
