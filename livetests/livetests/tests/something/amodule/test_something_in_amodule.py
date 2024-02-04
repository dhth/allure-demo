import allure
import pytest


class TestSomething:
    ############
    # SUCCESS #
    ############

    @allure.title("Test Something")
    @allure.description("This test tests something")
    @allure.tag("feature-1")
    def test_something(self, a_fake_fixture):
        assert a_fake_fixture == "fake"

    @allure.title("Test Something Parameterized")
    @allure.description("This test tests something that is parameterized")
    @allure.tag("feature-2")
    @pytest.mark.parametrize(
        "some_val",
        [
            ("val1"),
            ("val2"),
        ],
    )
    def test_something_parameterized(self, some_val):
        assert 1 == 1
