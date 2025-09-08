import pytest

from test.test_setuper import TestSetuper

def pytest_configure():
    TestSetuper.setup()

@pytest.fixture(autouse=True)
def per_test_setup_teardown():
    TestSetuper.delete_test_artifacts()
    yield
