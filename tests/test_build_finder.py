from src.apps.Jenkins.Application.Find.BuildFinder import BuildFinder
from src.apps.Jenkins.Infrastructure.ServerInMemoryRepository import ServerInMemoryRepository


class TestBuildFinder:
    def test_should_get_the_same_build_number(self):
        repository = ServerInMemoryRepository(
            queue_number=22,
            build_number=1,
            status="SUCCESS"
        )
        finder = BuildFinder(repository=repository)
        build_number = finder.number()

        assert build_number == 1

    def test_should_return_string_with_success_value(self):
        repository = ServerInMemoryRepository(
            queue_number=22,
            build_number=1,
            status="SUCCESS"
        )
        finder = BuildFinder(repository=repository)
        build_status = finder.exec(number=1)

        assert build_status == "SUCCESS"
