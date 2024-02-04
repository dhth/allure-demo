import allure
import pytest


@allure.title("Prepare a fake string")
@pytest.fixture(scope="session")
def a_fake_fixture():
    return "fake"


@allure.title("Prepare another fake string")
@pytest.fixture(scope="session")
def another_fake_fixture():
    return "more fake"
