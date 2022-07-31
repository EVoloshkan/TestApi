import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        help="This is request url"
    )

    parser.addoption(
        "--code",
        default=200,
        help="This is status code response"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def exp_code(request):
    return request.config.getoption("--code")
