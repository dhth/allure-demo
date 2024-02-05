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

    @allure.title("A new test")
    @allure.description("This test tests something new")
    @allure.tag("feature-3")
    def test_something_new(self, a_fake_fixture, another_fake_fixture):
        assert a_fake_fixture in another_fake_fixture

    @allure.title("Test something only on qa and staging")
    @allure.description("This test tests something only on qa and staging")
    @allure.tag("feature-3")
    def test_something_on_qa_and_staging(self, skip_for_prod):
        assert 2 == 2

    @allure.title("Test something only on qa")
    @allure.description("This test tests something only on qa")
    @allure.tag("feature-3")
    def test_something_only_on_qa(self, qa_only):
        assert 3 == 3

    @allure.title("Test something else only on qa")
    @allure.description("This test tests something else only on qa")
    @allure.tag("feature-4")
    def test_something_else_on_qa(self, qa_only):
        assert 4 == 4
