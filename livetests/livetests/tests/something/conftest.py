import pytest


@pytest.fixture(scope="session")
def a_fake_fixture():
    return "fake"
