import os

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


@pytest.fixture(scope="session")
def qa_only():
    if not os.environ.get("ENV", "qa") == "qa":
        pytest.skip("Skipped as qa only")


@pytest.fixture(scope="session")
def skip_for_prod():
    if os.environ.get("ENV", "qa") == "prod":
        pytest.skip("Skipped for prod")
