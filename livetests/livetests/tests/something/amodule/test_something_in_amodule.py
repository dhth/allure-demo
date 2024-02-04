import pytest


class TestSomething:
    ############
    # SUCCESS #
    ############

    def test_something(self, a_fake_fixture):
        assert a_fake_fixture == "fake"

    @pytest.mark.parametrize(
        "some_val",
        [
            ("val1"),
            ("val2"),
        ],
    )
    def test_something_parameterized(self, some_val):
        assert 1 == 1
