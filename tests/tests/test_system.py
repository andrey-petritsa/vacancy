from tests.helpers.app import App


class TestSystem:
    def test_healthcheck_back(self):
        assert App.check_back_health() == True

    def test_healthcheck_front(self):
        assert App.check_front_health() == True